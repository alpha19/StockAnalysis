from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFormLayout, QLineEdit
from gui.stock_button import StockButton

from PyQt5 import QtCore

__author__ = 'kdedow'

class SecureGui(QApplication):
    def __init__(self, argList=[]):
        super().__init__(argList)

        self.mainWindow = None
        self.stockWidget = None
        self.buttonWidget = None

        self.layout = None

        self.initialize()

    def initialize(self):
        self.mainWindow = QWidget()

        self.mainWindow.resize(500, 300)
        self.mainWindow.move(300, 300)
        self.mainWindow.setWindowTitle("Initial Stock Analysis Project")

        # Set the layout
        self.layout = QHBoxLayout()
        self.mainWindow.setLayout(self.layout)

        self._setupButtonWidget()

        self.mainWindow.show()

    def onAnalyzeClick(self):
        # TODO: There will eventually be analysis methods
        pass

    def onAddStockClick(self):
        pass

    def _setupStockWidget(self):
        self.stockWidget = QWidget()

        self.layout.addWidget(self.stockWidget)

    def _setupButtonWidget(self):
        # Setup the message box
        self.buttonWidget = QWidget(self.mainWindow)

        btnLayout = QFormLayout()
        btnLayout.setFormAlignment(QtCore.Qt.AlignRight)
        self.buttonWidget.setLayout(btnLayout)

        # Add the input dialog
        inputStock = QLineEdit("Enter Stock Symbol", self.buttonWidget)
        # TODO: Functionality for when add stock button is clicked

        # Setup the add stock button
        addStock = StockButton("Add Stock", self.buttonWidget)
        # TODO: Add a click action to add stock

        btnLayout.addRow(inputStock, addStock)
        self.layout.addWidget(self.buttonWidget)
        self.buttonWidget.show()
