import sys
# TODO: ALOT OF THIS STUFF MAY BE OBSOLETE (command line stuffs)
# TODO: Error handling. Also logging would be smart!
from gui.gui import SecureGui

__author__ = 'kdedow'

def main():
    #if security is not "":
    #    # TODO: Just focusing on stocks right now
    #    analysisObj = SecurityAnalysis(security)
    #    analysisObj.runAnalysis()
    with Database("../stocks.db") as db:
        app = SecureGui(sys.argv, db)
        sys.exit(app.exec_())

if __name__ == "__main__":
    main()

    """
    NOTE: The command line part has been commented out for now

    parser = OptionParser()
    parser.add_option("-s", "--security", dest="security", help="Security to analyze", default="")

    (opt, args) = parser.parse_args()
    sys.exit(main(opt.security))
    """
