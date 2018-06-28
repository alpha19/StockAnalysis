from abc import ABCMeta, abstractmethod
import time

__author__ = 'kdedow'

class SecurityInterface(object):
    """
    Interface for different types of securities

    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, secTarget=""):
        """

        :param secTarget:
        :return:
        """
        self.target = secTarget
        self.dateStr = time.strftime("%m/%d/%Y")

    @abstractmethod
    def queryAPI(self):
        """
        All subclasses must run some type of analysis
        :return:
        """
        pass

    @abstractmethod
    def getInfo(self):
        """
        Return formatted info about security (to be printed to console)
        :return:
        """
        pass

    @abstractmethod
    def updateInfo(self):
        pass
