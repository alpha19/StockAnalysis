import os
import smtplib
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding

__author__ = 'kdedow'

class Email(smtplib.SMTP_SSL):
    """
    This class provides a template from which an email can be sent.
    Gmail is used as the backend database
    """

    def __init__(self):
        smtplib.SMTP_SSL.__init__(self, 'smtp.gmail.com', 465)

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

        # Login

    def setMessageBody(self, message: str):
        pass

    def setRecipients(self, recipients):
        pass

    def setSubject(self, subject: str):
        pass

    def sendMessage(self):
        pass


