from ui.keyboard_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread


class Main(QtWidgets.QMainWindow, QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #  Object Setup
        self.ui.label_computer.setText('The quick brown fox')

        self.code_of_last_pressed_key = 63

    def keyPressEvent(self, event):
        self.code_of_last_pressed_key = event.key()
        print('DEC: ' + str(self.code_of_last_pressed_key))
        print('STR: ' + ''.join(chr(self.code_of_last_pressed_key)))
        self.update()

    def key_press_action(self):
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    supporttoolmain = Main()
    supporttoolmain.show()
    sys.exit(app.exec_())