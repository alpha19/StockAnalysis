import json

import requests
import time

from core.security_interface import SecurityInterface
from core.logging import Logging

__author__ = 'kdedow'

class Stock(SecurityInterface):
    """
    This class represents a stock object. Class members to store info about stock.
    Main objective of this class is to make API calls to keep stock info currently
    """
    BASE_URL = "https://api.iextrading.com/1.0/stock/"
    PERCENT_MULTIPLIER = 100

    def __init__(self, sec_target="",database=None):
        """

        :type sec_target: String
        :return:
        """
        SecurityInterface.__init__(self, sec_target)

        self.stockDB = database

        # Default instance variable
        self.company = ""
        self.curr = 0
        self.year_high = 0
        self.year_low = 0
        self.daily_percent = 0
        self.daily_change = 0

        self._initialize()

    # TODO: Change the name of this function. Should not be analyzing anything
    @Logging.SCOPE
    def queryAPI(self):
        """
        Update the given stock with current values
        :return:
        """

        # Setup the connections
        quoteData = json.loads(requests.get(Stock.BASE_URL + self.target + "/quote").text)

        self.company = quoteData['companyName']
        self.curr = quoteData['latestPrice']
        self.year_high = quoteData['week52High']
        self.year_low = quoteData['week52Low']
        self.daily_percent = Stock.PERCENT_MULTIPLIER * int(quoteData['changePercent'])
        self.daily_change = quoteData['change']

    def getInfo(self):
        info = "Basic Stock Info\n\n"
        info += "Company: " + self.company + "\n"
        info += "Current Price: {0}\n".format(str(self.curr))
        info += "Daily Change: {0}\n".format(str(self.daily_change))
        info += "Daily Percent Change: {0}\n".format(str(self.daily_percent))
        info += "Year High: {0}\n".format(str(self.year_high))
        info += "Year Low: {0}\n".format(str(self.year_low))

        return info

    # TODO: MIGHT WANT TO MOVE THIS METHOD INTO SECURITY ANALYSIS CLASS
    @Logging.SCOPE
    def updateInfo(self):
        # Query the yahoo API for current info
        self.queryAPI()

        # Update the values
        # TODO: NOT ALL VALUES NEED TO BE UPDATED -> DOING THIS FOR TESTING PURPOSES FOR NOW
        self.stockDB.query("UPDATE basic_info SET ticker = ? WHERE ticker = ?", (self.target, self.target))
        self.stockDB.query("UPDATE basic_info SET price = ? WHERE ticker = ?", (self.curr, self.target))
        self.stockDB.query("UPDATE basic_info SET daily_change = ? WHERE ticker = ?", (self.daily_change, self.target))
        self.stockDB.query("UPDATE basic_info SET daily_percent = ? WHERE ticker = ?", (self.daily_percent, self.target))
        self.stockDB.query("UPDATE basic_info SET company = ? WHERE ticker = ?", (self.company, self.target))
        self.stockDB.query("UPDATE basic_info SET year_high = ? WHERE ticker = ?", (self.year_high, self.target))
        self.stockDB.query("UPDATE basic_info SET year_low = ? WHERE ticker = ?", (self.year_low, self.target))
        self.stockDB.query("UPDATE basic_info SET date = ? WHERE ticker = ?", (self.dateStr, self.target))
        self.stockDB.query("UPDATE basic_info SET time = ? WHERE ticker = ?", (self.timeStr, self.target))

        # Now check the streak
        self._setStreaks()

    def _setStreaks(self):
        change = self.stockDB.query("SELECT daily_change FROM basic_info WHERE ticker=?", (self.target,))[0][0]
        currStreak = self.stockDB.query("SELECT streak FROM basic_info WHERE ticker=?", (self.target,))[0][0]

        dbDate = time.strptime(self.stockDB.query("SELECT date FROM basic_info WHERE ticker=?", (self.target,))[0][0], "%m/%d/%Y")
        currDate = time.localtime()

        # Only update if the date was updated a day or more ago
        if dbDate.tm_yday < currDate.tm_yday or dbDate.tm_year < currDate.tm_year:
            # First check prevents errors
            if currStreak is None:
                currStreak = 0

            if change < 0 and currStreak < 0:
                currStreak -= 1
            elif change < 0 and currStreak >= 0:
                currStreak = -1
            elif change > 0 and currStreak > 0:
                currStreak += 1
            else:
                currStreak = 1

        self.stockDB.query("UPDATE basic_info SET streak = ? WHERE ticker = ?", (currStreak, self.target))

    def _initialize(self):
        # Query the database (if it exists)
        if self.stockDB is not None:
            try:
                self.company = self.stockDB.query("SELECT company FROM basic_info WHERE ticker=?", (self.target,))[0][0]
                self.curr = self.stockDB.query("SELECT price FROM basic_info WHERE ticker=?", (self.target,))[0][0]
                self.year_high = self.stockDB.query("SELECT year_high FROM basic_info WHERE ticker=?", (self.target,))[0][0]
                self.year_low = self.stockDB.query("SELECT year_low FROM basic_info WHERE ticker=?", (self.target,))[0][0]
                self.daily_percent = self.stockDB.query("SELECT daily_percent FROM basic_info WHERE ticker=?", (self.target,))[0][0]
                self.daily_change = self.stockDB.query("SELECT daily_change FROM basic_info WHERE ticker=?", (self.target,))[0][0]
            except:
                # Don't worry about a database query failing, leave fields empty
                pass