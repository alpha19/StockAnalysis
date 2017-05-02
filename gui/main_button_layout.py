from PyQt5.QtWidgets import QWidget

__author__ = 'kdedow'

class MainButtons(QWidget):
    def __init__(self):
        super.__init__()

        self.quitButton = None
        self.trackButton = None
        self.ownedButton = None

        self.trackEntry = None
        self.ownedEntry = None

        self.initialize()

    def initialize(self):

