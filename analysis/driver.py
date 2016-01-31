import sys
from optparse import OptionParser
from analysis.security_analysis import SecurityAnalysis

__author__ = 'kdedow'

def main(security = ""):
    if security is not "":
        # TODO: Just focusing on stocks right now
        analysisObj = SecurityAnalysis(security)
        analysisObj.runAnalysis()


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-s", "--security", dest="security", help="Security to analyze", default="")

    (opt, args) = parser.parse_args()
    sys.exit(main(opt.security))
