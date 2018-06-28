from PyQt5.QtWidgets import QPushButton

__author__ = 'kdedow'

class StockButton(QPushButton):
    def __init__(self, name, widget):
        super().__init__(name, widget)

        self.resize(self.sizeHint())

    def setClickAction(self, action):
        pass
