import os
import sys

from PyQt5 import QtWidgets, uic

from controller.parent import ParentController
from controller.config import ConfigController

from worker.interval import IntervalWorker
from util.config import ConfigUtil

def main():
    app = QtWidgets.QApplication(sys.argv)

    window = uic.loadUi(os.path.join(os.path.dirname(__file__), 'ui', 'form.ui'))

    window.setWindowTitle('MySignage')
    window.resize(800, 480)

    cu = ConfigUtil()

    pc = ParentController(window, cu)
    cc = ConfigController(window, cu)

    iw = IntervalWorker(window, cu)

    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
