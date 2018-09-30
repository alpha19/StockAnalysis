import os

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding

__author__ = 'kdedow'

class Email(smtplib.SMTP_SSL):
    """
    This class provides a template from which an email can be sent.
    Gmail is used as the backend database
    """
    RECIPIENTS = ["kdedow@gmail.com"]

    def __init__(self):
        smtplib.SMTP_SSL.__init__(self, 'smtp.gmail.com', 465)

        self.message = MIMEMultipart('alternative')
        self.message['To'] = ", ".join(Email.RECIPIENTS)

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
        pem = os.getenv("HOME") + "/.ssh/id_rsa"
        with open(pem, "rb") as key_file:
            private_key = serialization.load_pem_private_key(key_file.read(),password=None,backend=default_backend())

        # Decrypt
        encrypt = os.getenv("HOME") + "/stock_email_credentials_encrypt.txt"
        with open(encrypt, "rb") as encrypt_file:
            cipher_text = encrypt_file.read()

        plain_text = private_key.decrypt(cipher_text, padding.PKCS1v15()).decode('UTF-8')
        login_creds = [text.strip() for text in plain_text.splitlines()]

        if len(login_creds) == 2:
            user = login_creds[0]
            password = login_creds[1]
            # Add to the email message
            self.message['From'] = user
        else:
            # TODO: Log a message
            pass

        # Login
        self.login(user, password)

    def addTextMessage(self, message: str):
        text = MIMEText(message, 'plain')
        self.message.attach(text)

    def addHTMLMessage(self, message: str):
        html = MIMEText(message, 'html')
        self.message.attach(html)

    def setRecipients(self, recipients):
        # Not planning on using this method since recipients is limited amount of people.
        # If this does ever need to be implemented, email recipients should be managed in
        # a database and this method should query database to get list of recipients
        pass

    def setSubject(self, subject: str):
        self.message['Subject'] = subject

    def sendMessage(self):
        self.sendmail(self.message.get('From'), self.message.get('To'), self.message.as_string())


