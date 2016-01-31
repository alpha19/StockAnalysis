from analysis.security_interface import SecurityInterface

__author__ = 'kdedow'

class Bond(SecurityInterface):
    """
    This class represents a bond object
    """

    def __init__(self, sec_target=""):
        """

        :type sec_target: String
        :return:
        """
        super().__init__(sec_target)

    def analyze(self):
        """
        Analyze the given stock
        :return:
        """