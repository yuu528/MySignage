import os
import sys

from PyQt5 import QtWidgets, uic

def main():
    app = QtWidgets.QApplication(sys.argv)

    window = uic.loadUi(os.path.join(os.path.dirname(__file__), 'ui', 'form.ui'))

    window.setWindowTitle('MySignage')
    window.resize(800, 480)

    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
