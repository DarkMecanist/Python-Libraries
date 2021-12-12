import unittest
import datetime
from ..py_gcp import GoogleCalendar


class TestInsertEvent(unittest.TestCase):
    """insert_event unit tests"""

    def setUp(self):
        self.calendar = GoogleCalendar(api_version="v3")

    def test_case_1(self):
        """Test inserting 30 minute event"""

        summary = "Test Event Summary"
        description = "Test Event Description"
        location = "Test Event Location"
        current_datetime = datetime.datetime.now()
        start_datetime = current_datetime + datetime.timedelta(days=1)
        end_datetime = current_datetime + datetime.timedelta(days=1, minutes=30)
        attendee_emails = ["jmoutinho94@gmail.com"]

        event = self.calendar.insert_event(summary, description, location, start_datetime, end_datetime, attendee_emails)

        self.assertEqual(event["status"], "confirmed")

        # Delete created Event
        self.calendar.service.events().delete(calendarId="primary", eventId=event["id"]).execute()


if __name__ == "__main__":
    unittest.main()
