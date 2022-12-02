from PyQt5.QtWidgets import *
from view import *
from random import randint

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    balance = int(100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.cardNumberTop.setText('')
        self.cardNumberMiddle.setText('')
        self.cardNumberBottom.setText('')
        self.errorLabel.setText('Choose High or Low\nLow (1-5) High (6-10)')
        self.LowButton.clicked.connect(lambda: self.playLow())
        self.HighButton.clicked.connect(lambda: self.playHigh())
        self.resetButton.clicked.connect(lambda: self.reset())

    def playLow(self, balance):
        # balance = int(100)
        self.balanceCounter.setText(f'test {balance}')
        number = randint(1, 10)
        if self.LowButton.clicked:
            if number > 5:
                self.winOrLoseLabel.setText(f'Sorry, you guessed wrong!\nThe number was {number}')
                balance = balance - 10
                self.balanceCounter.setText(f'{balance}')
                if balance < 1:
                    self.errorLabel.setText('You have a balance of 0\nClick reset to play again')
            if number < 6:
                self.winOrLoseLabel.setText('Congratulations, you won!\nClick High or Low to play again')
                balance = balance + 10
                self.balanceCounter.setText(f'{balance}')
                if balance < 1:
                    self.errorLabel.setText('You have a balance of 0\nClick reset to play again')

    def playHigh(self, balance):
        # balance = int(100)
        self.balanceCounter.setText(f'{balance}')
        number = randint(1, 10)
        if number > 5:
            self.winOrLoseLabel.setText('Congratulations, you won!\nClick High or Low to play again')
            balance = balance + 10
            self.balanceCounter.setText(f'{balance}')
            if balance < 1:
                self.errorLabel.setText('You have a balance of 0\nClick reset to play again')
        if number < 6:
            self.winOrLoseLabel.setText(f'Sorry, you guessed wrong!\nThe number was {number}')
            balance = balance - 10
            self.balanceCounter.setText(f'{balance}')
            if balance < 1:
                self.errorLabel.setText('You have a balance of 0\nClick reset to play again')

    def reset(self, balance):
        if balance == int(0):
            balance == int(100)
        else:
            self.errorLabel.setText('Balance must be zero before you can reset.')
