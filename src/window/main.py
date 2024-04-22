import os
from PyQt5 import QtWidgets, uic

import util.file as uf

main_ui = uic.loadUiType(os.path.join(uf.get_proj_dir(), 'src', 'ui', 'form.ui'))[0]

class MainWindow(QtWidgets.QWidget, main_ui):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)

        self.setWindowTitle('MySignage')
        self.resize(800, 480)
