from abc import ABCMeta, abstractmethod

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
        self._target = secTarget

    @abstractmethod
    def analyze(self):
        """
        All subclasses must run some type of analysis
        :return:
        """
        pass
