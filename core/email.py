import smtplib

__author__ = 'kdedow'

class Email(smtplib.SMTP_SSL):
    """
    This class provides a template from which an email can be sent.
    Gmail is used as the backend database
    """

    def __init__(self):
        super.__init__()

        self.ehlo()
        self.__login()

    def __login(self):
        # Read username and password from encrypted file.
        #   1. First read the file from users home directory.
        #   2. Then decrypt the file with users own private key
        #
        # Note: Any new users wishing to send emails can do so by creating a text file with
        #       email user name on first line and password on second line. Then encrypt with
        #       public/private key methodology

        # Read file

        # Decrypt

        # Login

    def setMessageBody(self, message: str):

    def setRecipients(self, recipients):

    def setSubject(self, subject: str):

    def sendMessage(self):


