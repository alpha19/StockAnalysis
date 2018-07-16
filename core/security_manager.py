import time

from core.security_types import SecurityTypes
from stocks.stock import Stock

__author__ = 'kdedow'

class SecurityManager(object):
    """
    Class to create and run analysis on a target security
    """
    def __init__(self, database=None):
        """
        :type secTarget: String
        """
        self.stockDB = database

    def Get(self, secTarget, secType=SecurityTypes.stock):
        """
        Creates a security object (e.g. stock bond)

        :return:
        """
        if secType is SecurityTypes.stock:
            # Create a stock object to run analysis on
            return Stock(secTarget, self.stockDB)
        else:
            # This shouldn't happen but return None if we can't find an appropriate security
            return None

    def setupStockTable(self):
        """
        Setup stocks table in db with initial stocks

        :return:
        """
        # Get the date
        date = datetime.date()
        dateStr = date.month() + "/" + date.day() + "/" + date.year()

        stocks = ("INTC", "AAPL", "GOOG", "YHOO", "SYK", "VZ")

        for stock in stocks:
            stockObj = self.securityFactory(stock)
            stockObj.queryAPI()

            self.stockDB.query("INSERT INTO basic_info (ticker, price, daily_change, company, year_high, year_low, \
             daily_percent, date, streak) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (stockObj.target, stockObj.curr, \
                                                                                stockObj.daily_change, stockObj.company,\
                                                                                stockObj.year_high, stockObj.year_low,\
                                                                                stockObj.daily_percent, dateStr, 0))

    def addStock(self, ticker=""):
        # Get the stock and analyze
        stockObj = self.Get(ticker)
        stockObj.queryAPI()

        # Store the stock in the db
        self.stockDB.query("INSERT INTO basic_info (ticker, price, daily_change, company, year_high, year_low, \
             daily_percent, date, streak) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (stockObj.target, stockObj.curr,
                                                                                stockObj.daily_change, stockObj.company,
                                                                                stockObj.year_high, stockObj.year_low,
                                                                                stockObj.daily_percent, stockObj.dateStr, 0))

    def removeStock(self, ticker=""):
        self.stockDB.query("DELETE FROM basic_info WHERE ticker=?", (ticker,))

    def updateStocks(self):
        """

        :return:
        """
        # Query the database for ticker symbols
        tickers = self.stockDB.query("SELECT ticker FROM basic_info")

        for stock in tickers:
            stockObj = self.Get(stock[0])
            stockObj.updateInfo()

    def getTrackedStocks(self):
        stocks = []

        tickers = self.stockDB.query("SELECT ticker FROM basic_info")

        for stock in tickers:
            stockObj = self.Get(stock[0])
            stocks.append(stockObj)

        return stocks




