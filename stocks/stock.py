import os
import re
import requests
import sqlite3
from analysis.security_interface import SecurityInterface

__author__ = 'kdedow'

class Stock(SecurityInterface):
    """
    This class represents a stock object
    """

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

        # Setup the connection
        desiredInfo = "nakjp2c1"
        resp = requests.get("http://finance.yahoo.com/d/quotes.csv?s=" + self.target + "&f=" + desiredInfo)

        # Get and parse the response, location in csv remains constant based on format
        # Only interested in the first line
        line = resp.text.splitlines()[0]
        if line is not None:
            stockCols = line.split(",")
            self.company = stockCols[0]
            self.curr = float(stockCols[1])
            self.year_high = float(stockCols[2])
            self.year_low = float(stockCols[3])

            # Percent change requires additional analysis
            percent = stockCols[4]
            percentVal = float(1)
            if percent.startswith("-"):
                percentVal = -1

            percent = re.sub('[-+%"]', '', percent)
            percentVal *= float(percent)

            self.daily_percent = percentVal

            # Same with daily change
            change = stockCols[5]
            changeVal = float(1)
            if(change.startswith("-")):
                changeVal = -1

            change = re.sub('[-+"]', '', change)
            changeVal *= float(change)

            self.daily_change = changeVal

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