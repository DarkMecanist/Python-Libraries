import os
import oauth2client
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools


class GoogleCloudPlatform:
    """
    GoogleCloudPlatform

    Available Scopes:
     - Google Calendar: https://www.googleapis.com/auth/calendar

    """

    def __init__(self, token_path, credentials_path, api):
        scopes = {
            "GoogleCalendar": ["https://www.googleapis.com/auth/calendar"]
        }

        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        temp_dir = "GoogleCloudPLatform/.temp"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        store = oauth2client.file.Storage(credentials_path)
        credentials = store.get()

        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets("credentials.json", scopes[api])




class GoogleCalendar(GoogleCloudPlatform):

    def __init__(self, token_path, credentials_path, scopes, version):
        super(GoogleCalendar, self).__init__(token_path, credentials_path, scopes)
        # self.service = build('calendar', version, credentials=self.creds)

    def insert_calendar_event(self):
        pass


token_path = "GoogleCloudPlatform/.temp/token.json"
credentials_path = "GoogleCloudPlatform/.temp/credentials.json"
api = "GoogleCalendar"
version = "v3"
calendar = GoogleCalendar(token_path, credentials_path, api, version)
