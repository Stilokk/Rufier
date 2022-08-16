from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QWidget, QGroupBox, QGridLayout,
                             QApplication, QPushButton, QListWidget, QLabel, QLineEdit)
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from instr import *
from second_win import *


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.iniUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def iniUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.bnt_next = QPushButton(txt_next, self)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.bnt_next, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

    def next_click(self):
        self.hide()
        self.tw = TestWin()

    def connects(self):
        self.bnt_next.clicked.connect(self.next_click)


app = QApplication([])
mw = MainWin()
app.exec_()
