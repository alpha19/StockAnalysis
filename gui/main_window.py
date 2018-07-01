from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QTableWidget, QTableWidgetItem

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
        self.buttonWidget = None

        self.layout = None

        self.initialize()

    def initialize(self):
        self.mainWindow = QWidget()

        self.mainWindow.resize(500, 300)
        self.mainWindow.move(300, 300)
        self.mainWindow.setWindowTitle("Tracked Stock Table")

        # Set the layout
        self.layout = QFormLayout()
        self.mainWindow.setLayout(self.layout)

        self._setupStockTable()
        self._setupButtonWidget()

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
        tableWidget = QTableWidget()

        # Add individual stocks
        stockAnalysis = SecurityManager(self.stockDB)
        stocks = stockAnalysis.getTrackedStocks()

        for row, stock in enumerate(stocks):
            self._createStockEntry(stock, row, tableWidget)

        # Add the header row
        tableHeaders = ["Ticker", "Price", "Daily Change", "Company", "Date"]
        tableWidget.setHorizontalHeaderLabels(tableHeaders)

        tableWidget.resizeColumnsToContents()
        tableWidget.resizeRowsToContents()

        tableLayout.addRow(tableWidget)
        tableWidget.show()

        self.layout.addRow(self.stockTable)
        self.stockTable.show()

    def _createStockEntry(self, stock, row, stockTable):
        stockColumns = []
        stockColumns.append(QTableWidgetItem(stock.target))
        stockColumns.append(QTableWidgetItem(stock.curr))
        stockColumns.append(QTableWidgetItem(stock.daily_change))
        stockColumns.append(QTableWidgetItem(stock.company))
        stockColumns.append(QTableWidgetItem(stock.dateStr))

        for col, item in enumerate(stockColumns):
            widgetItem = QTableWidgetItem(item)
            stockTable.setItem(row, col, widgetItem)

    def _setupButtonWidget(self):
        # Setup the message box
        self.buttonWidget = QWidget(self.mainWindow)

        btnLayout = QFormLayout()
        btnLayout.setFormAlignment(QtCore.Qt.AlignBottom)
        self.buttonWidget.setLayout(btnLayout)

        # Add the input dialog
        inputStock = QLineEdit("Ticker", self.buttonWidget)

        # Setup the add stock button
        addStock = StockButton("Add Stock", self.buttonWidget)

        # TODO: Add a click action to add stock

        btnLayout.addRow(inputStock, addStock)
        self.layout.addRow(self.buttonWidget)
        self.buttonWidget.show()
