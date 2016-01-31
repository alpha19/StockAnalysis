from analysis.security_types import SecurityTypes
from bonds.bond import Bond
from stocks.stock import Stock

__author__ = 'kdedow'

class SecurityAnalysis(object):
    """
    Class to create and run analysis on a target security
    """
    def __init__(self, secTarget="", secType=SecurityTypes.stock):
        """

        :type secTarget: String
        """
        self.__secureObj = self.__securityFactory(secTarget, secType)

    def __securityFactory(self, secTarget, secType):
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

    def runAnalysis(self):
        """

        """
        return self.__secureObj.analyze()


