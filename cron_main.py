from core.database_connection import Database
from core.security_manager import SecurityManager
from core.email import Email

from core.logging import Logging

__author__ = 'kdedow'

def main():
    # Setup Logging
    Logging.EnableLogger()
    Logging.SetFile(filename="stock_analysis_cron_main")

    Logging.DEBUG("Entering cron main.")

    with Database("../stocks.db") as db:
        Logging.DEBUG("Opened stock database successfully.")
        analysisObj = SecurityManager(db)
        # First update the stock table
        analysisObj.updateStocks()

        Logging.DEBUG("Succesfully updated tracked stocks.")
        # Now email the updated table to interested recipients
        # TODO: Deprectate this at some point as it is not useful to anyone really.
        email = Email()
        email.setSubject("Periodic Update from Stock Tracker Personal Project")
        email.addTextMessage("Here is your wonderful update. The list of tracked stocks was recently updated."
                             "Below you will find the most up to date info on the tracked stocks. Amazing.")
        email.addHTMLMessage(analysisObj.getHTMLTable())

        email.sendMessage()

if __name__ == "__main__":
    main()