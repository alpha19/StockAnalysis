#import sys
from analysis.security_analysis import SecurityAnalysis

__author__ = 'kdedow'

def main():
    analysisObj = SecurityAnalysis()
    analysisObj.updateStock()


if __name__ == "__main__":
    main()