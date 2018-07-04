from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QHBoxLayout, QLineEdit, QTableWidget, QTableWidgetItem

from core.security_manager import SecurityManager
from stocks.stock import Stock
from gui.stock_button import StockButton

__author__ = 'kdedow'

class SecureGui(QApplication):
    def __init__(self, argList=[], database=None):
        super().__init__(argList)

        self.stockDB = database

        self.mainWindow = None
        self.stockTable = None
        self.tableWidget = None
        self.buttonWidget = None
        self.formWidget = None

        self.layout = None

        self.initialize()

    def initialize(self):
        self.mainWindow = QWidget()

        self.mainWindow.resize(600, 300)
        self.mainWindow.move(300, 300)
        self.mainWindow.setWindowTitle("Tracked Stock Table")

        # Set the layout
        self.layout = QFormLayout()
        self.mainWindow.setLayout(self.layout)

        self._setupStockTable()
        self._setupButtonWidgets()

        self.mainWindow.show()

    def onAnalyzeClick(self):
        # TODO: There will eventually be analysis methods
        pass

    def onAddStockClick(self):
        # Adds a new stock to the stock database.
        pass

    def _setupStockTable(self):
        self.stockTable = QWidget()

        tableLayout = QFormLayout()
        tableLayout.setFormAlignment(QtCore.Qt.AlignTop)
        self.stockTable.setLayout(tableLayout)

        # Add the actual table
        self.tableWidget = QTableWidget()

        # Add individual stocks
        tableHeaders = ["Ticker", "Price", "Daily Change", "Daily Percent", "Year High", "Year Low", "Company", "Date"]

        stockAnalysis = SecurityManager(self.stockDB)
        stocks = stockAnalysis.getTrackedStocks()

        self.tableWidget.setRowCount(len(stocks))
        self.tableWidget.setColumnCount(len(tableHeaders))

        for row, stock in enumerate(stocks):
            self._createStockEntry(stock, row)

        # Add the header row
        self.tableWidget.setHorizontalHeaderLabels(tableHeaders)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        tableLayout.addRow(self.tableWidget)
        self.tableWidget.show()

        self.layout.addRow(self.stockTable)
        self.stockTable.show()

    def _createStockEntry(self, stock, row):
        stockColumns = []
        stockColumns.append(QTableWidgetItem(stock.target))
        stockColumns.append(QTableWidgetItem(str(stock.curr)))
        stockColumns.append(QTableWidgetItem(str(stock.daily_change)))
        # Convert percent from decimal value and round to 4 significant digits
        stockColumns.append(QTableWidgetItem(str(round(100*stock.daily_percent,4))))
        stockColumns.append(QTableWidgetItem(str(stock.year_high)))
        stockColumns.append(QTableWidgetItem(str(stock.year_low)))
        stockColumns.append(QTableWidgetItem(stock.company))
        stockColumns.append(QTableWidgetItem(stock.dateStr))

        for col, item in enumerate(stockColumns):
            widgetItem = QTableWidgetItem(item)
            self.tableWidget.setItem(row, col, widgetItem)

    def _setupButtonWidgets(self):
        # Setup the message box
        self.buttonWidget = QWidget(self.mainWindow)
        self.formWidget = QWidget(self.mainWindow)

        btnLayout = QHBoxLayout()
        btnLayout.setAlignment(QtCore.Qt.AlignBottom)
        self.buttonWidget.setLayout(btnLayout)

        formLayout = QHBoxLayout()
        formLayout.setAlignment(QtCore.Qt.AlignBottom)
        self.formWidget.setLayout(formLayout)

        # Add the input dialog
        inputStock = QLineEdit("Ticker", self.buttonWidget)
        inputStock.setMaximumWidth(100)

        # Setup the add stock button
        addStock = StockButton("Add Stock", self.buttonWidget)

        # Implements support for adding a new stock to DB
        def addStockAction():
            stockAnalysis = SecurityManager(self.stockDB)
            stockAnalysis.addStock(inputStock.text())

            stock = stockAnalysis.Get(inputStock.text())

            self.tableWidget.insertRow(self.tableWidget.rowCount())
            self._createStockEntry(stock, self.tableWidget.rowCount()-1)

        addStock.clicked.connect(addStockAction)

        # Add remove stock button
        removeStock = StockButton("Remove Stock", self.buttonWidget)

        # Implements support for adding a new stock to DB
        def removeStockAction():
            stockAnalysis = SecurityManager(self.stockDB)
            stockAnalysis.removeStock(inputStock.text())

            stocks = stockAnalysis.getTrackedStocks()

            self.tableWidget.setRowCount(len(stocks))

            for row, stock in enumerate(stocks):
                self._createStockEntry(stock, row)

        removeStock.clicked.connect(removeStockAction)

        # Add update stock button
        updateStock = StockButton("Update Stock(s)", self.buttonWidget)

        # Implements support for updating the stock table entry
        def updateStockAction():
            stockAnalysis = SecurityManager(self.stockDB)
            stockAnalysis.updateStocks()

            stocks = stockAnalysis.getTrackedStocks()

            self.tableWidget.setRowCount(len(stocks))

            for row, stock in enumerate(stocks):
                self._createStockEntry(stock, row)

        updateStock.clicked.connect(updateStockAction)

        formLayout.addWidget(inputStock)

        btnLayout.addWidget(addStock)
        btnLayout.addWidget(removeStock)
        btnLayout.addWidget(updateStock)

        self.layout.addRow(self.buttonWidget)
        self.layout.addRow(self.formWidget)

        self.buttonWidget.show()
