import sqlite3
import os
import time
from analysis.security_types import SecurityTypes
from bonds.bond import Bond
from stocks.stock import Stock

#TODO: RETHINK THIS WHOLE CLASS

__author__ = 'kdedow'

class SecurityAnalysis(object):
    """
    Class to create and run analysis on a target security
    """
    def __init__(self):
        """
        :type secTarget: String
        """
        pass

    def securityFactory(self, secTarget, secType=SecurityTypes.stock):
        """
        Creates a security object (e.g. stock bond

        :return:
        """
        if secType is SecurityTypes.stock:
            # Create a stock object to run analysis on
            return Stock(secTarget)
        elif secType is SecurityTypes.bond:
            # Create a bond object to run analysis on. Also this isn't really a security...
            return Bond(secTarget)

    def setupStockTable(self):
        """
        Setup stocks table in db with initial stocks

        :return:
        """
        # Get the date
        date = datetime.date()
        dateStr = date.month() + "/" + date.day() + "/" + date.year()

        # open the connection
        dir_path = os.path.dirname(os.path.abspath(__file__))
        conn = sqlite3.connect(os.path.join(dir_path, '../stocks.db'))

        stocks = ("INTC", "AAPL", "GOOG", "YHOO", "SYK", "VZ")

        for stock in stocks:
            stockObj = self.securityFactory(stock)
            stockObj.analyze()

            conn.execute("INSERT INTO basic_info (ticker, price, daily_change, company, year_high, year_low, \
             daily_percent, date, streak) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (stockObj.target, stockObj.curr, \
                                                                                stockObj.daily_change, stockObj.company,\
                                                                                stockObj.year_high, stockObj.year_low,\
                                                                                stockObj.daily_percent, dateStr, 0))

        # Close the connection
        conn.commit()
        conn.close()

    def addStock(self, ticker = ""):
        # Get the date
        dateStr = time.strftime("%d/%m/%Y")

        # Get the stock and analyze
        stockObj = self.securityFactory(ticker)
        stockObj.analyze()

        # open the connection
        dir_path = os.path.dirname(os.path.abspath(__file__))
        conn = sqlite3.connect(os.path.join(dir_path, '../stocks.db'))

        # Store the stock in the db
        conn.execute("INSERT INTO basic_info (ticker, price, daily_change, company, year_high, year_low, \
             daily_percent, date, streak) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (stockObj.target, stockObj.curr, \
                                                                                stockObj.daily_change, stockObj.company,\
                                                                                stockObj.year_high, stockObj.year_low,\
                                                                                stockObj.daily_percent, dateStr, 0))
        # Close the connection
        conn.commit()
        conn.close()


    def updateStock(self):
        """

        :return:
        """
        # open the connection, get ticker values, close connection
        dir_path = os.path.dirname(os.path.abspath(__file__))
        conn = sqlite3.connect(os.path.join(dir_path, '../stocks.db'))
        tickers = conn.execute("SELECT ticker FROM basic_info").fetchall()

        for stock in tickers:
            stockObj = self.securityFactory(stock[0])
            stockObj.storeInfo()

        conn.close()




