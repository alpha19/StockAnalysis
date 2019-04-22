"""


_author__ = kdedow

"""

import logging
import datetime

class Logging:
    DEFAULT_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    @staticmethod
    def EnableLogger():
        logging.basicConfig(format=Logging.DEFAULT_FORMAT, level=logging.DEBUG, datefmt='%d-%b-%y %H:%M:%S')

    @staticmethod
    def DisableLogger():
        pass

    @staticmethod
    def SetFile(filename="general_stock_analysis_log"):
        filename += "_{date:%Y-%m-%d %H:%M:%S}.log".format(date=datetime.datetime.now())

        handle = logging.FileHandler("/var/logs/" + filename, 'w')
        handle.setFormatter(logging.Formatter(Logging.DEFAULT_FORMAT))

        log = logging.getLogger()

        for hdl in log.handlers[:]:
            log.removeHandler(hdl)

        log.addHandler(handle)


    @staticmethod
    def SetLogLevel(level=logging.DEBUG):
        pass

    @staticmethod
    def Debug(msg=""):
        logging.debug(msg)
