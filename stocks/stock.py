import json
import os
import sqlite3

import requests

from core import strings
from analysis.security_interface import SecurityInterface

__author__ = 'kdedow'

class Stock(SecurityInterface):
    """
    This class represents a stock object. Class members to store info about stock.
    Main objective of this class is to make API calls to keep stock info currently
    """
    BASE_URL = "https://api.iextrading.com/1.0/stock/"

    def __init__(self, sec_target=""):
        """

        :type sec_target: String
        :return:
        """
        SecurityInterface.__init__(self, sec_target)

        # Default instance variable
        self.company = ""
        self.curr = 0
        self.year_high = 0
        self.year_low = 0
        self.daily_percent = 0
        self.daily_change = 0

    # TODO: Change the name of this function. Should not be analyzing anything
    def analyze(self):
        """
        Analyze the given stock
        :return:
        """

        # Setup the connections
        quoteData = json.loads(requests.get(Stock.BASE_URL + self.target + "/quote").text)

        self.company = quoteData['companyName']
        self.curr = quoteData['latestPrice']
        self.year_high = quoteData['week52High']
        self.year_low = quoteData['week52Low']
        self.daily_percent = quoteData['changePercent']
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
    def storeInfo(self):
        # Query the yahoo API for current info
        self.analyze()

        # open the connection
        dir_path = os.path.dirname(os.path.abspath(__file__))
        conn = sqlite3.connect(os.path.join(dir_path, '../stocks.db'))

        # Update the values
        # TODO: NOT ALL VALUES NEED TO BE UPDATED -> DOING THIS FOR TESTING PURPOSES FOR NOW
        conn.execute("UPDATE basic_info SET ticker = ? WHERE ticker = ?", (self.target, self.target))
        conn.execute("UPDATE basic_info SET price = ? WHERE ticker = ?", (self.curr, self.target))
        conn.execute("UPDATE basic_info SET daily_change = ? WHERE ticker = ?", (self.daily_change, self.target))
        conn.execute("UPDATE basic_info SET daily_percent = ? WHERE ticker = ?", (self.daily_percent, self.target))
        conn.execute("UPDATE basic_info SET company = ? WHERE ticker = ?", (self.company, self.target))
        conn.execute("UPDATE basic_info SET year_high = ? WHERE ticker = ?", (self.year_high, self.target))
        conn.execute("UPDATE basic_info SET year_low = ? WHERE ticker = ?", (self.year_low, self.target))
        conn.execute("UPDATE basic_info SET date = ? WHERE ticker = ?", (self.dateStr, self.target))

        # Now check the streak
        self.setStreaks(conn)

        conn.commit()
        conn.close()

    def setStreaks(self, conn):
        change = conn.execute("SELECT daily_change FROM basic_info WHERE ticker=?", (self.target,)).fetchall()[0][0]
        currStreak = conn.execute("SELECT streak FROM basic_info WHERE ticker=?", (self.target,)).fetchall()[0][0]

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

        conn.execute("UPDATE basic_info SET streak = ? WHERE ticker = ?", (currStreak, self.target))

    def _initialize(self):
        # open the connection
        dir_path = os.path.dirname(os.path.abspath(__file__))
        conn = sqlite3.connect(os.path.join(dir_path, '../stocks.db'))

        self.company = conn.execute("SELECT company FROM basic_info WHERE ticker=?", (self.target,)).fetchall()[0][0]
        self.curr = conn.execute("SELECT price FROM basic_info WHERE ticker=?", (self.target,)).fetchall()[0][0]
        self.year_high = conn.execute("SELECT year_high FROM basic_info WHERE ticker=?", (self.target,)).fetchall()[0][0]
        self.year_low = conn.execute("SELECT year_low FROM basic_info WHERE ticker=?", (self.target,)).fetchall()[0][0]
        self.daily_percent = conn.execute("SELECT daily_percent FROM basic_info WHERE ticker=?", (self.target,)).fetchall()[0][0]
        self.daily_change = conn.execute("SELECT daily_change FROM basic_info WHERE ticker=?", (self.target,)).fetchall()[0][0]

        conn.close()