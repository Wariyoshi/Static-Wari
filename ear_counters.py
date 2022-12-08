import math
from PyQt5.QtWidgets import *
from view import *

class Ear_Counters(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.Submit_Button.clicked.connect(lambda: self.submit())
        self.Clear_Button.clicked.connect(lambda: self.clear_form())

    def human_ears(self, n):
        if n > 0:
            return 2 + self.human_ears(n - 1)
        else:
            return 0

    def alien_ears(self, n):
        if n > 0:
            if (n % 2) == 1:
                return 2 + self.alien_ears(n - 1)
            else:
                return 3 + self.alien_ears(n - 1)
        else:
            return 0

    def cost(self, ear_human, ear_alien):
        total_qtips = math.ceil(ear_human + ear_alien)
        if total_qtips < 0:
            raise RuntimeError
        elif total_qtips < 500:
            return total_qtips * 0.01
        elif total_qtips < 1000:
            return ((math.floor(total_qtips / 500) * 4) + ((total_qtips % 500) * 0.01))
        else:
            return ((math.floor(total_qtips / 1000) * 7) + ((total_qtips % 1000) * 0.01))

    def submit(self):
        human_clients = 0
        alien_clients = 0
        try:
            if self.Human_Entry.text() == '':
                human_clients = 0
            else: #not empty string - numbers or actual strings
                human_clients = int(self.Human_Entry.text())
                if human_clients < 0:
                    raise Exception
        except ValueError:
            self.Human_Entry.setText('')
            self.Instructions_Label.setText('Please only use Earthling Arabic numerals!')
        except Exception:
            self.Human_Entry.setText('')
            self.Instructions_Label.setText('Please only use positive numbers!')
        else:
            try:
                if self.Alien_Entry.text() == '':
                    alien_clients = 0
                else:
                    alien_clients = int(self.Alien_Entry.text())
                    if alien_clients < 0:
                        raise Exception
            except ValueError:
                self.Alien_Entry.setText('')
                self.Instructions_Label.setText('Please only use Earthling Arabic numerals!')
            except Exception:
                self.Alien_Entry.setText('')
                self.Instructions_Label.setText('Please only use positive numbers!')
            else:
                totalEars = self.human_ears(human_clients) + self.alien_ears(alien_clients)
                self.Instructions_Label.setText(
                    f'You will need {totalEars} Q-tips and they will cost ${self.cost(self.human_ears(human_clients), self.alien_ears(alien_clients)):.02f} in total.')

    def clear_form(self):
        self.Human_Entry.setText('')
        self.Alien_Entry.setText('')
        self.Instructions_Label.setText('Welcome to the ENT Office Q-tip budget calculator, Doctor!\n'
                                        '\nUnfortunately, this application has no function to translate \nalien numbers. Please submit Arabic numerals denoting how '
                                        '\nmany clients you have of each species and this calculator will \ndetermine how much money you will need to spend on Q-tips \nto clean their ears!\n'
                                        '\nNote: Individual Q-tips cost $0.01 each, however boxes of \n500 cost $4.00 each and boxes of 1000 cost $7.00 each.'
                                        '\nThis program will pick the best deal for you!')