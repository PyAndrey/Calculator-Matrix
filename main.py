# -------------Version Alpha 3.1----------------#
import sys

from PyQt5 import QtWidgets

from calculate import UiMainWindow
from calculate_3x3 import UiMainWindow as UiMainWindow_3x3


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui_3x3 = UiMainWindow_3x3()
        self.ui = UiMainWindow()
        self.start_ui()

    def start_ui_3x3(self):
        self.ui_3x3.setupUi(self)
        self.ui_3x3.action.triggered.connect(self.start_ui)
        self.show()

    def start_ui(self):
        self.ui.setupUi(self)
        self.ui.action_3x3.triggered.connect(self.start_ui_3x3)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    # Run mainloop
    sys.exit(app.exec())
