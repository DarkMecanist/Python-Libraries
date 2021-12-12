import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request


class GoogleCloudPlatform:
    """
    GoogleCloudPlatform

    Available Scopes:
     - Google Calendar: https://www.googleapis.com/auth/calendar

    """

    def __init__(self, api_name, api_version, scopes, client_secret_file):
        credentials = None
        pickle_file = f'token_{api_name}_{api_version}.pickle'
        temp_dir = os.path.join(os.getcwd(), ".temp")

        if not os.path.exists(temp_dir):
            os.mkdir(temp_dir)

        if os.path.exists(os.path.join(temp_dir, pickle_file)):
            with open(os.path.join(temp_dir, pickle_file), "rb") as token:
                credentials = pickle.load(token)

        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                if os.path.exists(os.path.join(temp_dir, client_secret_file)):
                    flow = InstalledAppFlow.from_client_secrets_file(os.path.join(temp_dir, client_secret_file), scopes)
                    credentials = flow.run_local_server()
                else:
                    raise Exception(f"No file {client_secret_file} in dir {temp_dir}")

            with open(os.path.join(temp_dir, pickle_file), "wb") as token:
                pickle.dump(credentials, token)

        try:
            self.service = build(api_name, api_version, credentials=credentials)
            print(f"{api_name}, {api_version} service created successfully.")
        except Exception as e:
            os.remove(os.path.join(temp_dir, pickle_file))
            raise e


class GoogleCalendar(GoogleCloudPlatform):
    """
    Google Calendar API

    Available Scopes:
        "https://www.googleapis.com/auth/calendar"
    """

    def __init__(self, api_version):
        api_name = "calendar"
        scopes = ["https://www.googleapis.com/auth/calendar"]
        client_secret_file = "client_secret.json"
        super(GoogleCalendar, self).__init__(api_name, api_version, scopes, client_secret_file)

    def insert_event(self, summary, description, location, start_datetime, end_datetime,
                              attendee_emails, start_timezone="America/Los_Angeles", end_timezone="America/Los_Angeles",
                              recurrence_rules=None, reminders=None):
        """
        :param summary: [String]
        :param description: [String]
        :param location: [String]
        :param start_datetime: [DateTime]
        :param start_timezone: [String]
        :param end_datetime: [Datetime]
        :param end_timezone: [String]
        :param recurrence_rules: [List: String]
        :param attendee_emails: [List: String]
        :param reminders: [List: Dictionary]
        example reminders: [{"method": "email", "minutes": 30}, {"method": "popup", "minutes": 10}]
        :return: Dictionary
        """

        if not summary:
            raise Exception("Summary not provided.")

        if not description:
            raise Exception("Description not provided.")

        if not location:
            raise Exception("Location not provided.")

        if not start_datetime:
            raise Exception("Start DateTime nor provided.")

        if not end_datetime:
            raise Exception("End DateTime not provided.")

        if not attendee_emails:
            raise Exception("Attendee Emails not provided.")

        if not recurrence_rules:
            recurrence_rules = ["RRULE:FREQ=DAILY;COUNT=1"]

        if not reminders:
            reminders = [
                {"method": "email", "minutes": 24 * 60},
                {"method": "popup", "minutes": 10}
            ]

        event_info = {
            "summary": summary,
            "description": description,
            "start": {
                "dateTime": f"{start_datetime.year}-{start_datetime.month}-{start_datetime.day}T"
                            f"{start_datetime.hour-1}:{start_datetime.minute}:00-00:00",
                "timeZone": start_timezone,
            },
            "end": {
                "dateTime": f"{end_datetime.year}-{end_datetime.month}-{end_datetime.day}T"
                            f"{end_datetime.hour-1}:{end_datetime.minute}:00-00:00",
                "timeZone": end_timezone,
            },
            "recurrence": recurrence_rules,
            "attendees": [{"email": email} for email in attendee_emails],
            "reminders": {
                "useDefault": False,
                "overrides": reminders
            }
        }

        event = self.service.events().insert(calendarId="primary", body=event_info).execute()

        print(f"Event created successfully ({event.get('htmlLink')})")

        return event

