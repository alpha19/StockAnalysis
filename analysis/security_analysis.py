import sqlite3
from analysis.security_types import SecurityTypes
from bonds.bond import Bond
from stocks.stock import Stock

#TODO: RETHINK THIS WHOLE METHOD

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
            # Create a bond object to run analysis on
            return Bond(secTarget)

    def setupStockTable(self):
        """
        Setup stocks table in db with initial stocks

        :return:
        """
        # open the connection
        conn = sqlite3.connect('../stocks.db')

        stocks = ("INTC", "AAPL", "GOOG", "YHOO", "SYK", "VZ")

        for stock in stocks:
            stockObj = self.securityFactory(stock)
            stockObj.analyze()

            conn.execute("INSERT INTO basic_info (ticker, price, daily_change, company, year_high, year_low, \
             daily_percent) VALUES (?, ?, ?, ?, ?, ?, ?)", (stockObj.target, stockObj.curr, stockObj.daily_change, \
                                                            stockObj.company, stockObj.year_high, stockObj.year_low,\
                                                            stockObj.daily_percent))


        conn.commit()
        conn.close()

    def addStock(self):
        pass

    def updateStock(self):
        """

        :return:
        """
        # open the connection, get ticker values, close connection
        conn = sqlite3.connect('../stocks.db')
        tickers = conn.execute("SELECT ticker FROM basic_info").fetchall()

        for stock in tickers:
            stockObj = self.securityFactory(stock[0])
            stockObj.storeInfo()

        conn.close()




