from analysis.security_analysis import SecurityAnalysis

__author__ = 'kdedow'

def main():
    with Database("../stocks.db") as db:
        analysisObj = SecurityAnalysis(db)
        analysisObj.updateStock()

if __name__ == "__main__":
    main()