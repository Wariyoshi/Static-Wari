import math
from PyQt5.QtWidgets import *
from view import *

class Ear_Counters(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.Submit_Button.clicked.connect(lambda: self.submit())
        self.Clear_Button.clicked.connect(lambda: self.clear_form())

    def human_ears(n):
        if n > 0:
            return 2 + human_ears(n - 1)
        else:
            return 0

    def alien_ears(n):
        if n > 0:
            if (n % 2) == 1:
                return 2 + alien_ears(n - 1)
            else:
                return 3 + alien_ears(n - 1)
        else:
            return 0

    def cost(self, ear_human, ear_alien):
        self.total_qtips = math.ceil(self.ear_human + self.ear_alien)
        if self.total_qtips < 0:
            raise RuntimeError
        elif self.total_qtips < 500:
            return self.total_qtips * 0.01
        elif self.total_qtips < 1000:
            return ((math.floor(self.total_qtips / 500) * 4) + ((self.total_qtips % 500) * 0.01))
        else:
            return ((math.floor(self.total_qtips / 1000) * 7) + ((self.total_qtips % 1000) * 0.01) )

    def submit(self):
        try:
            self.human_clients = int(self.Human_Entry.text())
        except ValueError:
            if self.Human_Entry.text() == '':
                self.human_clients = 0
            else:
                self.Human_Entry.setText('')
                self.Instructions_Label.setText('Please only use Earthling Arabic numerals!')
        else:
            try:
                self.alien_clients = int(self.Alien_Entry.text())
            except ValueError:
                if self.Alien_Entry.text() == '':
                    self.alien_clients = 0
                else:
                    self.Alien_Entry.setText('')
                    self.Instructions_Label.setText('Please only use Earthling Arabic numerals!')
            else:
                try:
                    self.Instructions_Label.setText(f'You will need {human_ears(human_clients) + alien_ears(alien_clients)} Q-tips and they will cost {cost(human_ears(human_clients), alien_ears(alien_clients)):.02f} in total.')
                except RuntimeError:
                    self.Instructions_Label.setText('It\'s not possible for you to have negative patients!')

    def clear_form(self):
        self.Human_Entry.setText('')
        self.Alien_Entry.setText('')
        self.Instructions_Label.setText('Welcome to the ENT Office Q-tip budget calculator, Doctor!\n\nUnfortunately, this application has no function to translate \nalien numbers. Please submit Arabic numerals denoting how \nmany clients you have of each species and this calculator will \ndetermine how much money you will need to spend on Q-tips \nto clean their ears!\n\nNote: Individual Q-tips cost $0.01 each, however boxes of \n500 cost $4.00 each and boxes of 1000 cost $7.00 each.\nThis program will pick the best deal for you!')