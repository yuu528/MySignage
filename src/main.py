import os
import sys

from PyQt5 import QtWidgets, uic

from window.main import MainWindow

from controller.parent import ParentController
from controller.config import ConfigController

from worker.interval import IntervalWorker
from util.config import ConfigUtil

class MySignage:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)

        self.window = MainWindow()

        self.cu = ConfigUtil()

        self.pc = ParentController(self)
        self.cc = ConfigController(self)
        self.iw = IntervalWorker(self)

        self.window.show()

def main():
    ms = MySignage()
    sys.exit(ms.app.exec_())

if __name__ == '__main__':
    main()
