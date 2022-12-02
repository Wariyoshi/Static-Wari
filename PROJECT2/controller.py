from PyQt5.QtWidgets import *
from view import *
from random import randint

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    balance = 100

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.cardNumberTop.setText('')
        self.cardNumberMiddle.setText('')
        self.cardNumberBottom.setText('')
        self.errorLabel.setText('Choose High or Low\nLow (1-5) High (6-10)')
        self.LowButton.clicked.connect(lambda: self.playGame())
        self.HighButton.clicked.connect(lambda: self.playGame())

    def playGame(self):
        balance = 100
        while balance != 0:
            number = randint(1, 10)
            if self.LowButton.clicked:
                if number > 5:
                    self.winOrLoseLabel.setText('Congratulations, you won!\nClick High or Low to play again')
