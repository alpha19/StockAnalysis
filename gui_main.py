import sys
# TODO: Error handling. Also logging would be smart!
from gui.main_window import SecureGui
from core.database_connection import Database

__author__ = 'kdedow'

def main():
    #    # TODO: Just focusing on stocks right now
    with Database("../stocks.db") as db:
        app = SecureGui(sys.argv, db)
        ret = app.exec_()

    sys.exit(ret)

if __name__ == "__main__":
    main()

    """
    NOTE: The command line part has been commented out for now

    parser = OptionParser()
    parser.add_option("-s", "--security", dest="security", help="Security to analyze", default="")

    (opt, args) = parser.parse_args()
    sys.exit(main(opt.security))
    """
