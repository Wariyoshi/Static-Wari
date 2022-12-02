from ear_counters import *

def main():
    app = QApplication([])
    window = Ear_Counters()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
