from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QWidget, QGroupBox, QGridLayout,
                             QApplication, QPushButton, QListWidget, QLabel, QLineEdit)
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from instr import *


class FinalWin(QWidget):
    def __init__(self, exp):

        self.exp = exp

        super().__init__()
        self.set_appear()
        self.iniUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def results(self):
        if self.exp.person.line_name2 < 7:
            self.index = 0
            return
        self.index = (4 * (int(self.exp.line_name3) + int(self.exp.line_name4) + int(self.exp.line_name5)) - 200) / 10
        if self.exp.person.line_name2 == 7 or self.exp.person.line_name2 == 8:
            if self.index >= 21:
                return txt_res1
            elif self.index < 21 and self.index >= 17:
                return txt_res2
            elif self.index < 17 and self.index >= 12:
                return txt_res3
            elif self.index < 12 and self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.person.line_name2 == 9 or self.exp.person.line_name2 == 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index < 19.5 and self.index >= 15.5:
                return txt_res2
            elif self.index < 15.5 and self.index >= 10.5:
                return txt_res3
            elif self.index < 10.5 and self.index >= 5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.person.line_name2 == 11 or self.exp.person.line_name2 == 12:
            if self.index >= 18:
                return txt_res1
            elif self.index < 18 and self.index >= 14:
                return txt_res2
            elif self.index < 14 and self.index >= 9:
                return txt_res3
            elif self.index < 9 and self.index >= 3.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.person.line_name2 == 13 or self.exp.person.line_name2 == 14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index < 16.5 and self.index >= 12.5:
                return txt_res2
            elif self.index < 12.5 and self.index >= 7.5:
                return txt_res3
            elif self.index < 7.5 and self.index >= 2:
                return txt_res4
            else:
                return txt_res5

        if self.exp.person.line_name2 >= 15:
            if self.index < 15 and self.index >= 11:
                return txt_res1
            elif self.index < 15 and self.index >= 11:
                return txt_res2
            elif self.index < 11 and self.index >= 6:
                return txt_res3
            elif self.index < 6 and self.index >= 0.5:
                return txt_res4
            else:
                return txt_res5

    def iniUI(self):
        self.work = QLabel(txt_workheart + self.results())
        self.txt_index = QLabel(txt_index + str(self.index))


        self.final_line = QVBoxLayout()
        self.final_line.addWidget(self.txt_index, alignment=Qt.AlignCenter)
        self.final_line.addWidget(self.work, alignment=Qt.AlignCenter)
        self.setLayout(self.final_line)
