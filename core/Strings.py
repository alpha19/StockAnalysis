import re

"""
This file contains various string helper functions
"""
__author__ = 'kdedow'

def StringToFloat(numericStr: str):
    '''

    :param numericStr: The string to convert to a float
    :return:
    '''
    numVal = float(1)

    if numericStr.startswith("-"):
        numVal = -1

    numericStr = re.sub('[-+%"]', '', numericStr)
    numVal *= float(numericStr)
    return numVal