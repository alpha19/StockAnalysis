

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

__author__ = 'kdedow'

class SecureGui(QApplication):
    def __init__(self):
        super.__init__(self, [])

        self.mainWindow = None
        self.buttonWidget = None

        self.initialize()

    def initialize(self):
        self.mainWindow = QWidget()

        self.mainWindow.resize(250, 150)
        self.mainWindow.move(300, 300)
        self.mainWindow.setWindowTitle("Initial Stock Analysis Project")
        self.mainWindow.show()

        self.buttonWidget = Main

    def onAnalyzeClick(self):
        # TODO: There will eventually be analysis methods
        pass

    def onAddStockClick(self):
        pass
