# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculate_3x3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import numpy as np
from PyQt5 import QtCore, QtWidgets

from matrix import matrix_3x3
from utils import *


class UiMainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 332)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(510, 332))
        MainWindow.setMaximumSize(QtCore.QSize(510, 332))
        MainWindow.setFocusPolicy(QtCore.Qt.TabFocus)
        MainWindow.setStyleSheet("QPushButton{\n"
"    height: 50px;\n"
"    background-color: white;\n"
"    font-size: 12px;\n"
"    border: none;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: silver;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:rgb(159, 159, 159)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(510, 280))
        self.centralwidget.setMaximumSize(QtCore.QSize(510, 291))
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 481, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 5, 3, 55)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 3, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(50, 35))
        self.lineEdit_4.setFrame(False)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 1, 4, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_5.setFrame(False)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 1, 3, 1, 1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_1.setMaximumSize(QtCore.QSize(50, 35))
        self.lineEdit_1.setBaseSize(QtCore.QSize(0, 0))
        self.lineEdit_1.setFrame(False)
        self.lineEdit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 0, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(20, 140))
        self.label_2.setStyleSheet(".QLabel{\n"
"    margin: 0;\n"
"    padding: 0;\n"
"    height: 0;\n"
"    border: none;\n"
"    border-left: 1px solid #333;\n"
"}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 3, 1)
        self.labe_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labe_1.sizePolicy().hasHeightForWidth())
        self.labe_1.setSizePolicy(sizePolicy)
        self.labe_1.setMaximumSize(QtCore.QSize(20, 140))
        self.labe_1.setTabletTracking(False)
        self.labe_1.setStyleSheet(".QLabel{\n"
"    margin: 0;\n"
"    padding: 0;\n"
"    height: 0;\n"
"    border: none;\n"
"    border-right: 1px solid #333;\n"
"}")
        self.labe_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labe_1.setText("")
        self.labe_1.setObjectName("labe_1")
        self.gridLayout.addWidget(self.labe_1, 0, 5, 3, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setBaseSize(QtCore.QSize(0, 0))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 3, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 0, 2, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_6.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_6.setFrame(False)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 1, 2, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(50, 35))
        self.lineEdit_7.setFrame(False)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 2, 4, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_8.setMaximumSize(QtCore.QSize(50, 35))
        self.lineEdit_8.setFrame(False)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 2, 3, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_9.setMaximumSize(QtCore.QSize(50, 35))
        self.lineEdit_9.setFrame(False)
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 2, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())
        self.pushButton.clicked.connect(self.calculate)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.lineEdit_2.setText(_translate("MainWindow", "5"))
        self.lineEdit_4.setText(_translate("MainWindow", "6"))
        self.lineEdit_5.setText(_translate("MainWindow", "8"))
        self.lineEdit_1.setText(_translate("MainWindow", "2"))
        self.label_3.setText(_translate("MainWindow", "="))
        self.lineEdit_3.setText(_translate("MainWindow", "4"))
        self.lineEdit_6.setText(_translate("MainWindow", "5"))
        self.lineEdit_7.setText(_translate("MainWindow", "6"))
        self.lineEdit_8.setText(_translate("MainWindow", "4"))
        self.lineEdit_9.setText(_translate("MainWindow", "5"))
        self.pushButton.setText(_translate("MainWindow", "Расчитать"))
        self.menu.setTitle(_translate("MainWindow", "Режим"))
        self.action.setText(_translate("MainWindow", "Режим уравнения"))

    def calculate(self):
        lineedits = {"lineedit_1": self.lineEdit_1,
                     "lineedit_2": self.lineEdit_2,
                     "lineedit_3": self.lineEdit_3,
                     "lineedit_4": self.lineEdit_4,
                     "lineedit_5": self.lineEdit_5,
                     "lineedit_6": self.lineEdit_6,
                     "lineedit_7": self.lineEdit_7,
                     "lineedit_8": self.lineEdit_8,
                     "lineedit_9": self.lineEdit_9}

        # Преобразует в строку value, потом в число.
        value_to_int = bypass_list([value.text() for name, value in lineedits.items()])

        a1 = value_to_int[:3]  # Строка верхняя
        a2 = value_to_int[3:6]  # Строка посередине
        a3 = value_to_int[6:10]  # Строка нижняя

        matrix = np.array([a1, a2, a3])  # Многоуровневый список

        res = matrix_3x3(matrix)  # Расчет результата

        if res is not None:
            self.label_3.setText(f"= {res}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

