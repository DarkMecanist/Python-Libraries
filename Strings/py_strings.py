import re


class Strings:
    """

        """

    def __init__(self):
        self.regex_email = "[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}"

    def is_valid_email(self, email):
        """
        :param email: [String]
        :return: [Boolean]

        Description: Checks if an the email string is a valid email format
        """

        if str(re.match(self.regex_email, email, re.IGNORECASE)) != "None":
            print(f"Email: {email} is valid.")
            return True
        else:
            print(f"Email: {email} is not valid.")
            return False
