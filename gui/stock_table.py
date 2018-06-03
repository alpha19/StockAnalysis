from PyQt5.QtWidgets import QListWidget

__author__ = 'kdedow'

class StockList(QListWidget):
    def __init__(self, widget):
        super().__init__(widget)

        self.resize(self.sizeHint())

