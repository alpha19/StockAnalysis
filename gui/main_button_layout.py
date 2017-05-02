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
        # Now setup quit button
        self.quitButton = QPushButton('Quit', self.mainWindow)
        self.quitButton.clicked.connect(QCoreApplication.instance().quit)
        self.quitButton.resize(qbtn.sizeHint())
        self.quitButton.move(50, 50)

        # Now the analysis buttonw
        self.trackButton('Track')

