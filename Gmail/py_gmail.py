import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from Strings.py_strings import Strings


class Gmail:
    """Gmail methods"""

    def __init__(self, account_email, account_password):
        self.account_email = account_email
        self.account_password = account_password
        self.smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)

    def send_email(self, emails_to, subject, body, attachments=[]):
        """
        :param emails_to: [List] emails to send
        :param subject: [String]
        :param body: [String]
        :param attachments: [List] file_paths
        """

        # Check emails_to not empty
        if len(emails_to) == 0:
            raise Exception("No emails provided.")

        # Check subject not empty
        if str(subject) == "":
            raise Exception("No subject provided.")

        # Check body not empty
        if str(body) == "":
            raise Exception("No body provided.")

        # Check if all emails are valid
        for email in emails_to:
            is_valid_email = Strings().is_valid_email(email)
            if not is_valid_email:
                raise Exception(f"{email} is not a valid email.")

        email_message = MIMEMultipart()
        email_message["From"] = self.account_email
        email_message["To"] = COMMASPACE.join(emails_to)
        email_message["Date"] = formatdate(localtime=True)
        email_message["Subject"] = subject
        email_message.attach(MIMEText(body))

        for attachment in attachments:
            with open(attachment, "rb") as file:
                part = MIMEApplication(file.read(), Name=basename(attachment))

            part["Content-Disposition"] = f'attachment; filename="{basename(attachment)}"'
            email_message.attach(part)

        with self.smtp_obj as sp:
            sp.ehlo()
            sp.starttls()
            sp.ehlo()
            sp.login(self.account_email, self.account_password)
            sp.sendmail(self.account_email, emails_to, email_message.as_string())
