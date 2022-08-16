from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QWidget, QGroupBox, QGridLayout,
                             QApplication, QPushButton, QListWidget, QLabel, QLineEdit)
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont

from instr import *
from final_win import *


class Person():
    def __init__(self, line_name1, line_name2):
        self.line_name1 = line_name1
        self.line_name2 = line_name2


class Experiment():
    def __init__(self, person, line_name3, line_name4, line_name5):
        self.person = person
        self.line_name3 = line_name3
        self.line_name4 = line_name4
        self.line_name5 = line_name5


class TestWin(QWidget):
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
        self.text_name = QLabel(txt_name)
        self.line_name1 = QLineEdit(txt_hintname)
        self.txt_age = QLabel(txt_age)
        self.line_name2 = QLineEdit(txt_hintage)
        self.txt_test1 = QLabel(txt_test1)
        self.btn_test1 = QPushButton(txt_starttest1, self)
        self.line_name3 = QLineEdit(txt_hinttest1)
        self.txt_test2 = QLabel(txt_test2)
        self.btn_test2 = QPushButton(txt_starttest2, self)
        self.txt_test3 = QLabel(txt_test3)
        self.btn_test3 = QPushButton(txt_starttest3, self)
        self.line_name4 = QLineEdit(txt_hinttest2)
        self.line_name5 = QLineEdit(txt_hinttest3)
        self.btn_test4 = QPushButton(txt_sendresults)
        self.text_timer = QLabel(txt_timer)

        self.r_line = QVBoxLayout()
        self.r_line.addWidget(self.text_name, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.line_name1, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.txt_age, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.line_name2, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.txt_test1, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.btn_test1, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.line_name3, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.txt_test2, alignment=Qt.AlignLeft)
        self.l_line = QVBoxLayout()
        self.l_line.addWidget(self.text_timer, alignment=Qt.AlignRight)
        self.r_line.addLayout(self.l_line)
        self.r_line.addWidget(self.btn_test2, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.txt_test3, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.btn_test3, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.line_name4, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.line_name5, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.btn_test4, alignment=Qt.AlignCenter)
        self.setLayout(self.l_line)
        self.setLayout(self.r_line)

    def next_click(self):
        self.hide()
        self.prs = Person(self.line_name1.text, int(self.line_name2.text()))
        self.exp = Experiment(self.prs, self.line_name3.text(), self.line_name4.text(), self.line_name5.text())
        self.tw = FinalWin(self.exp)

    def timer_test1(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss')[6:8])
        self.text_timer.setStyleSheet("color: rgb(0,0,0")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_bob(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)

        self.timer.start(1500)

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color:rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color:rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color:rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def connects(self):
        self.btn_test4.clicked.connect(self.next_click)
        self.btn_test1.clicked.connect(self.timer_test1)
        self.btn_test2.clicked.connect(self.timer_bob)
        self.btn_test3.clicked.connect(self.timer_final)
