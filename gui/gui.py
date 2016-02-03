import Tkinter
from analysis.security_analysis import SecurityAnalysis

__author__ = 'kdedow'

class SecureGui(Tkinter.Tk):
    def __init__(self, parent=None):
        Tkinter.Tk.__init__(self, parent)

        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable=self.entryVariable)
        self.entry.grid(column = 0, row = 0, sticky = 'EW')
        self.entryVariable.set(u"Enter Ticker Symbol")

        buttonOne = Tkinter.Button(self,text = u"Analyze", command=self.onAnalyzeClick)
        buttonOne.grid(column = 1, row = 0)

        buttonTwo = Tkinter.Button(self,text = u"Add Stock", command=self.onAddStockClick)
        buttonTwo.grid(column = 1, row = 1)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self, textvariable=self.labelVariable, anchor = "w",fg = "black",bg = "white")
        label.grid(column=0,row=2,columnspan=2,sticky='EW')

        self.grid_columnconfigure(0, weight = 1)
        self.resizable(True, False)

    def onAnalyzeClick(self):
        stock = self.entryVariable.get()

        # Get the stock info
        if stock is not "" or "Enter Ticker Symbol":
            # TODO: Just focusing on stocks right now
            analysisObj = SecurityAnalysis()

            securitiesObj = analysisObj.securityFactory(stock)
            securitiesObj.analyze()
            info = securitiesObj.getInfo()

            self.labelVariable.set(info)

    def onAddStockClick(self):
        stock = self.entryVariable.get()

        # Get the stock info
        if stock is not "" or "Enter Ticker Symbol":
            # TODO: Just focusing on stocks right now
            analysisObj = SecurityAnalysis()

            securitiesObj = analysisObj.addStock(stock)

        # Not sure if this is robust enough yet
        print("Successfully added " + stock + " to database")