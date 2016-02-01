from analysis.security_interface import SecurityInterface
import requests
import sqlite3

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

    def analyze(self):
        """
        Analyze the given stock
        :return:
        """

        # Setup the connection
        resp = requests.get("http://finance.yahoo.com/webservice/v1/symbols/" + self.target + "/quote?format=json&view=detail")

        # Get and parse the response
        info = resp.json()['list']['resources'][0]['resource']['fields']

        self.company = info['name']
        self.curr = float(info['price'])
        self.year_high = float(info['year_high'])
        self.year_low = float(info['year_low'])
        self.daily_percent = float(info['chg_percent'])
        self.daily_change = float(info['change'])

    def getInfo(self):
        info = "Basic Stock Info\n\n"
        info += "Company: " + self.company + "\n"
        info += "Current Price: {0}\n".format(str(self.curr))
        info += "Daily Change: {0}\n".format(str(self.daily_change))
        info += "Daily Percent Change: {0}\n".format(str(self.daily_percent))
        info += "Year High: {0}\n".format(str(self.year_high))
        info += "Year Low: {0}\n".format(str(self.year_low))

        return info

    def storeInfo(self):
        # Query the yahoo API for current info
        self.analyze()

        # open the connection
        conn = sqlite3.connect('../stocks.db')

        # Update the values
        # TODO: NOT ALL VALUES NEED TO BE UPDATED -> DOING THIS FOR TESTING PURPOSES FOR NOW
        conn.execute("UPDATE basic_info SET ticker = ? WHERE ticker = ?", (self.target, self.target))
        conn.execute("UPDATE basic_info SET price = ? WHERE ticker = ?", (self.curr, self.target))
        conn.execute("UPDATE basic_info SET daily_change = ? WHERE ticker = ?", (self.daily_change, self.target))
        conn.execute("UPDATE basic_info SET daily_percent = ? WHERE ticker = ?", (self.daily_percent, self.target))
        conn.execute("UPDATE basic_info SET company = ? WHERE ticker = ?", (self.company, self.target))
        conn.execute("UPDATE basic_info SET year_high = ? WHERE ticker = ?", (self.year_high, self.target))
        conn.execute("UPDATE basic_info SET year_low = ? WHERE ticker = ?", (self.year_low, self.target))

        conn.commit()
        conn.close()