# -------------Version Alpha 2.6----------------#
import sys

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

from calculate import Ui_MainWindow
from calculate_3x3 import Ui_MainWindow as Ui_MainWindow_3x3
from matrix import matrix_3x3

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui_3x3 = Ui_MainWindow_3x3()
        self.ui = Ui_MainWindow()
        self.startUI()

    def startUI_3x3(self):
        self.ui_3x3.setupUi(self)
        self.ui_3x3.action.triggered.connect(self.startUI)
        self.show()

    def startUI(self):
        self.ui.setupUi(self)
        self.ui.action_3x3.triggered.connect(self.startUI_3x3)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    # Run mainloop
    sys.exit(app.exec_())
