#import sys
from analysis.security_analysis import SecurityAnalysis
from analysis.security_interface import SecurityInterface

__author__ = 'kdedow'

def main():
    analysisObj = SecurityAnalysis()
    analysisObj.updateStock()


if __name__ == "__main__":
    main()