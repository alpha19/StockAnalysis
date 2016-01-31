from analysis.security_interface import SecurityInterface
import requests

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
        super().__init__(sec_target)

    def analyze(self):
        """
        Analyze the given stock
        :return:
        """

        # Setup the connection
        resp = requests.get("http://finance.yahoo.com/webservice/v1/symbols/" + self._target + "/quote?format=json&view=detail")

        # Get and parse the response
        info = resp.json()['list']['resources'][0]['resource']['fields']
        company = info['name']
        curr = info['price']
        year_high = info['year_high']
        year_low = info['year_low']

        # Spit some basic info to console
        print("Basic Stock Info\n")
        print("\tCompany: " + company)
        print("\tCurrent Price: " + curr)
        print("\tYear High: " + year_high)
        print("\tYear Low: " + year_low)

