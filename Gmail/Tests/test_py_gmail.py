import unittest
import os
from ..py_gmail import Gmail


class TestsSendEmail(unittest.TestCase):
    """send_email unit tests"""

    def setUp(self):
        self.gmail = Gmail(str(os.environ["EMAIL_USER"]), str(os.environ["EMAIL_PASSWORD"]))
        print(os.environ["EMAIL_USER"])
        print(os.environ["EMAIL_PASSWORD"])

    def test_case_1(self):
        """Testing with a single valid email and no attachments"""

        emails_to = ["jmoutinho94@gmail.com"]
        subject = "Email sent from python"
        body = """Python Gmail Library
        test_case_1
        """

        self.gmail.send_email(emails_to, subject, body)

    def test_case_2(self):
        """Testing with multiple valid emails and attachments"""

        emails_to = ["jmoutinho94@gmail.com", "joao.moutinho@farfetch.com"]
        subject = "Email sent from python"
        body = """Python Gmail Library
        test_case_2
        """
        attachments = ["Gmail/Data/test.txt"]

        print(os.getcwd())

        self.gmail.send_email(emails_to, subject, body, attachments)


if __name__ == "__main__":
    unittest.main()