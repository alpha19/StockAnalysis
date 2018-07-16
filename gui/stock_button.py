from PyQt5.QtWidgets import QPushButton

from threading import Thread

__author__ = 'kdedow'

class StockButton(QPushButton):
    def __init__(self, name, widget):
        super().__init__(name, widget)

        self.resize(self.sizeHint())
        self.setMaximumWidth(150)

    def setClickAction(self, method):
        def runThread():
            thread = Thread(target=method)
            thread.start()

        self.clicked.connect(runThread)



