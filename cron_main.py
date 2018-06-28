from core.database_connection import Database
from core.security_manager import SecurityManager

__author__ = 'kdedow'

def main():
    with Database("../stocks.db") as db:
        analysisObj = SecurityManager(db)
        analysisObj.updateStocks()

if __name__ == "__main__":
    main()