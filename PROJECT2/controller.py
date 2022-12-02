from PyQt5.QtWidgets import *
from view import *
from random import randint

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):

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
        self.balance = int(100)

    def playLow(self):
        # self.balanceCounter.setText(f'test {self.balance}')
        self.errorLabel.setText('Choose High or Low\nLow (1-5) High (6-10)')
        number = randint(1, 10)
        self.cardNumberTop.setText(f'{number}')
        self.cardNumberMiddle.setText(f'{number}')
        self.cardNumberBottom.setText(f'{number}')
        # while self.balance > int(0):  # Look back at this!
        if number > 5:
            self.winOrLoseLabel.setText(f'Sorry, you guessed wrong!\nThe number was {number}')
            self.balance = self.balance - 10
            self.balanceCounter.setText(f'{self.balance}')
            if self.balance < 1:
                self.errorLabel.setText('You have a balance of 0\nClick reset to play again')
        if number < 6:
            self.winOrLoseLabel.setText('Congratulations, you won!\nClick High or Low to play again')
            self.balance = self.balance + 10
            self.balanceCounter.setText(f'{self.balance}')
            if self.balance < 1:
                self.errorLabel.setText('You have a balance of 0\nClick reset to play again')

    def playHigh(self):
        # self.balanceCounter.setText(f'{self.balance}')
        self.errorLabel.setText('Choose High or Low\nLow (1-5) High (6-10)')
        number = randint(1, 10)
        self.cardNumberTop.setText(f'{number}')
        self.cardNumberMiddle.setText(f'{number}')
        self.cardNumberBottom.setText(f'{number}')
        if number > 5:
            self.winOrLoseLabel.setText('Congratulations, you won!\nClick High or Low to play again')
            self.balance = self.balance + 10
            self.balanceCounter.setText(f'{self.balance}')
            if self.balance < 1:
                self.errorLabel.setText('You have a balance of 0\nClick reset to play again')
        if number < 6:
            self.winOrLoseLabel.setText(f'Sorry, you guessed wrong!\nThe number was {number}')
            self.balance = self.balance - 10
            self.balanceCounter.setText(f'{self.balance}')
            if self.balance < 1:
                self.errorLabel.setText('You have a balance of 0\nClick reset to play again')

    def reset(self):
        if self.balance == int(0):
            self.balance = self.balance + 100
            self.balanceCounter.setText(f'{self.balance}')
        else:
            self.errorLabel.setText('Balance must be zero before you can reset.')
