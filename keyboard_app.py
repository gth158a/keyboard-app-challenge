from ui.keyboard_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread


class Main(QtWidgets.QMainWindow, QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.user_type = ''

        #  Object Setup
        self.ui.label_computer.setText('The quick brown fox')

        self.code_of_last_pressed_key = 63

    def keyPressEvent(self, event):
        self.code_of_last_pressed_key = event.key()
        self.key_press_action(self.code_of_last_pressed_key)
        self.user_type = self.user_type + ''.join(chr(self.code_of_last_pressed_key))
        self.ui.label_user.setText(self.user_type)
        print(self.user_type)
        self.update()

    def key_press_action(self, key):
        if key == 76:
            self.ui.key_l.animateClick()
        elif key == 49:
            self.ui.key_1.animateClick()
        elif key == 50:
            self.ui.key_2.animateClick()
        elif key == 51:
            self.ui.key_3.animateClick()
        elif key == 52:
            self.ui.key_4.animateClick()
        elif key == 53:
            self.ui.key_5.animateClick()
        elif key == 54:
            self.ui.key_6.animateClick()
        elif key == 55:
            self.ui.key_7.animateClick()
        elif key == 56:
            self.ui.key_8.animateClick()
        elif key == 57:
            self.ui.key_9.animateClick()
        elif key == 48:
            self.ui.key_0.animateClick()
        elif key == 81:
            self.ui.key_q.animateClick()
        elif key == 87:
            self.ui.key_w.animateClick()
        elif key == 69:
            self.ui.key_e.animateClick()
        elif key == 82:
            self.ui.key_r.animateClick()
        elif key == 84:
            self.ui.key_t.animateClick()
        elif key == 89:
            self.ui.key_y.animateClick()
        elif key == 85:
            self.ui.key_u.animateClick()
        elif key == 73:
            self.ui.key_i.animateClick()
        elif key == 79:
            self.ui.key_o.animateClick()
        elif key == 80:
            self.ui.key_p.animateClick()
        elif key == 65:
            self.ui.key_a.animateClick()
        elif key == 83:
            self.ui.key_s.animateClick()
        elif key == 68:
            self.ui.key_d.animateClick()
        elif key == 70:
            self.ui.key_f.animateClick()
        elif key == 71:
            self.ui.key_g.animateClick()
        elif key == 72:
            self.ui.key_h.animateClick()
        elif key == 74:
            self.ui.key_j.animateClick()
        elif key == 75:
            self.ui.key_k.animateClick()
        elif key == 76:
            self.ui.key_l.animateClick()
        elif key == 90:
            self.ui.key_z.animateClick()
        elif key == 88:
            self.ui.key_x.animateClick()
        elif key == 67:
            self.ui.key_c.animateClick()
        elif key == 86:
            self.ui.key_v.animateClick()
        elif key == 66:
            self.ui.key_b.animateClick()
        elif key == 78:
            self.ui.key_n.animateClick()
        elif key == 77:
            self.ui.key_m.animateClick()
        elif key == 44:
            self.ui.key_comma.animateClick()
        elif key == 46:
            self.ui.key_dot.animateClick()
        elif key == 47:
            self.ui.key_forward_slash.animateClick()
        elif key == 96:
            self.ui.key_tilde.animateClick()
        elif key == 45:
            self.ui.key_dash.animateClick()
        elif key == 61:
            self.ui.key_equals.animateClick()
        elif key == 91:
            self.ui.key_sqrbrkt_left.animateClick()
        elif key == 93:
            self.ui.key_sqrbrkt_right.animateClick()
        elif key == 92:
            self.ui.key_back_slash.animateClick()
        elif key == 59:
            self.ui.key_semicolon.animateClick()
        elif key == 39:
            self.ui.key_apostrophe.animateClick()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    supporttoolmain = Main()
    supporttoolmain.show()
    sys.exit(app.exec_())