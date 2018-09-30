from core.database_connection import Database
from core.security_manager import SecurityManager
from core.email import Email

__author__ = 'kdedow'

def main():
    with Database("../stocks.db") as db:
        analysisObj = SecurityManager(db)
        # First update the stock table
        analysisObj.updateStocks()

        # Now email the updated table to interested recipients
        # TODO: Format the actual email body and subject with the tracked stock table!!!
        email = Email()
        email.setSubject("This is a subject")
        email.addTextMessage("This is the message")

        email.sendMessage()

if __name__ == "__main__":
    main()