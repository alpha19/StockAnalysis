import sys
from optparse import OptionParser
from analysis.security_analysis import SecurityAnalysis
from gui.gui import SecureGui

__author__ = 'kdedow'

def main(security = ""):
    if security is not "":
        # TODO: Just focusing on stocks right now
        analysisObj = SecurityAnalysis(security)
        analysisObj.runAnalysis()


if __name__ == "__main__":
    app = SecureGui()
    app.title('Basic Stock Info')
    app.mainloop()

    """
    NOTE: The command line part has been commented out for now

    parser = OptionParser()
    parser.add_option("-s", "--security", dest="security", help="Security to analyze", default="")

    (opt, args) = parser.parse_args()
    sys.exit(main(opt.security))
    """
