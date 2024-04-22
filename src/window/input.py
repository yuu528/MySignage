import os
from PyQt5 import QtCore, QtWidgets, uic

import util.file as uf

input_ui = uic.loadUiType(os.path.join(uf.get_proj_dir(), 'src', 'ui', 'input_dialog.ui'))[0]

class InputDialog(QtWidgets.QDialog, input_ui):
    def __init__(self, parent, title, input_type, max=None):
        super(InputDialog, self).__init__(parent)

        self.input_type = input_type

        self.setupUi(self)

        self.setWindowTitle("Input Dialog")
        self.setWindowFlags(QtCore.Qt.Window)
        self.resize(800, 480)

        self.title.setText(title)

        if self.input_type == 'int':
            self.stackedWidget.setCurrentIndex(0)

            self.btnp.setHidden(True)

            self.spinBox.setMinimum(0)
            self.spinBox.setMaximum(max)
        elif self.input_type == 'float':
            self.stackedWidget.setCurrentIndex(1)

            self.btnp.setHidden(False)

            self.doubleSpinBox.setMinimum(0)
            self.doubleSpinBox.setMaximum(max)

        self.btne.clicked.connect(self.enter)
        self.btnc.clicked.connect(self.reject)

        self.btn0.clicked.connect(lambda: self.click(0))
        self.btn1.clicked.connect(lambda: self.click(1))
        self.btn2.clicked.connect(lambda: self.click(2))
        self.btn3.clicked.connect(lambda: self.click(3))
        self.btn4.clicked.connect(lambda: self.click(4))
        self.btn5.clicked.connect(lambda: self.click(5))
        self.btn6.clicked.connect(lambda: self.click(6))
        self.btn7.clicked.connect(lambda: self.click(7))
        self.btn8.clicked.connect(lambda: self.click(8))
        self.btn9.clicked.connect(lambda: self.click(9))
        self.btnp.clicked.connect(lambda: self.click('.'))
        self.btnb.clicked.connect(lambda: self.click(-1))

        # -1: normal, 0: point pressed, 1 <: inputting decimals
        self.point = -1

    def enter(self):
        if self.input_type == 'int':
            self.returnVal = self.spinBox.value()
        elif self.input_type == 'float':
            self.returnVal = self.doubleSpinBox.value()

        self.accept()

    def click(self, val):
        if self.input_type == 'int':
            if val == -1:
                self.spinBox.setValue(self.spinBox.value() // 10)
            else:
                self.spinBox.setValue(self.spinBox.value() * 10 + val)
        elif self.input_type == 'float':
            if val == '.':
                if self.point < 0:
                    self.point = 0
            elif val == -1:
                if self.point > 0:
                    box_val = self.doubleSpinBox.value()

                    dig = box_val * (10 ** self.point) % 10
                    box_val -= dig / (10 ** self.point)

                    self.point -= 1
                else:
                    box_val = self.doubleSpinBox.value() // 10

                if self.point == 0:
                    self.point = -1

                self.doubleSpinBox.setValue(box_val)
            else:
                if self.point >= 0:
                    if self.point == 0:
                        self.point = 1
                    elif self.point > 0:
                        self.point += 1

                    self.doubleSpinBox.setValue(self.doubleSpinBox.value() + val / (10 ** self.point))
                else:
                    self.doubleSpinBox.setValue(self.doubleSpinBox.value() * 10 + val)
