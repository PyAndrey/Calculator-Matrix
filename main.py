# -------------Version Alpha 2.6----------------#

import sys

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

from matrix import matrix_3x3
from calculate_3x3 import Ui_MainWindow as Ui_MainWindow_3x3
from calculate import Ui_MainWindow

# Create application
app = QtWidgets.QApplication(sys.argv)

# Create form and init UI
MainWindow = QtWidgets.QMainWindow()


def bypass_list(list):
    """Обходит список, преобразует в int, если строка выводит ошибку."""
    list1 = []
    for i in list:
        try:
            list1.append(int(i))
        except ValueError:
            raise ValueError
    return list1


class WindowMatrix3x3():
    """Создаёт окно калькулятора матрицы 3 на 3"""

    def __init__(self):
        self.ui_3x3 = Ui_MainWindow_3x3()
        self.ui_3x3.setupUi(MainWindow)
        self.pressed_button()
        self.ui_3x3.pushButton.clicked.connect(self.calculate)
        MainWindow.show()

    def pressed_button(self):
        self.ui_3x3.action.triggered.connect(WindowEquation)

    def calculate(self):
        lineedits = {"lineedit_1": self.ui_3x3.lineEdit_1,
                     "lineedit_2": self.ui_3x3.lineEdit_2,
                     "lineedit_3": self.ui_3x3.lineEdit_3,
                     "lineedit_4": self.ui_3x3.lineEdit_4,
                     "lineedit_5": self.ui_3x3.lineEdit_5,
                     "lineedit_6": self.ui_3x3.lineEdit_6,
                     "lineedit_7": self.ui_3x3.lineEdit_7,
                     "lineedit_8": self.ui_3x3.lineEdit_8,
                     "lineedit_9": self.ui_3x3.lineEdit_9}

        # Преобразует в строку value, потом в число.
        list = bypass_list([value.text() for name, value in lineedits.items()])

        a1 = list[:3] # Строка верхняя
        a2 = list[3:6] # Строка посередине
        a3 = list[6:10] # Строка нижняя

        matrix = np.array([a1, a2, a3]) # Многоуровневый список

        res = matrix_determinant_2x2(matrix) # Расчет результата

        if res is not None:
            self.ui_3x3.label_3.setText(str(res))


class WindowEquation():
    """Создает окно системы уравнений."""

    def __init__(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.pressed_button()
        self.ui.pushButton.clicked.connect(self.calculate)
        MainWindow.show()

    def pressed_button(self):
        self.ui.action_3x3.triggered.connect(WindowMatrix3x3)

    def calculate(self):
        lineedits = {"lineedit_1": self.ui.lineEdit_1,
                     "lineedit_2": self.ui.lineEdit_2,
                     "lineedit_3": self.ui.lineEdit_3,
                     "lineedit_4": self.ui.lineEdit_4,
                     "lineEdit_5": self.ui.lineEdit_5,
                     "lineEdit_6": self.ui.lineEdit_6,
                     "lineEdit_7": self.ui.lineEdit_7,
                     "lineEdit_8": self.ui.lineEdit_8,
                     "lineEdit_9": self.ui.lineEdit_9,
                     "lineEdit_10": self.ui.lineEdit_10,
                     "lineEdit_11": self.ui.lineEdit_11,
                     "lineEdit_12": self.ui.lineEdit_12}
        # Преобразует в строку value, потом в число.
        list = bypass_list([value.text() for name, value in lineedits.items()])

        a1 = list[:4] # Строка верхняя
        a2 = list[4:8] # Строка посередине
        a3 = list[8:12] # Строка нижняя

        matrix = np.array([a1, a2, a3]) # Многоуровневый список

        determinant = []
        determinant.append(matrix_3x3(matrix)) # Записывается результат матрицы

        for i in range(3):
            list1, list2, list3 = a1.copy(), a2.copy(), a3.copy() # Копируются строки
            # Идет замена каждого элемента для расчетов.
            list1[i] = list1[3]
            list2[i] = list2[3]
            list3[i] = list3[3]

            matrix = np.array([list1, list2, list3]) # Многоуровневый список

            determinant.append(matrix_3x3(matrix)) # Записывается результат матриц

        # Сравнение и вычисление x1, x2, x3
        if determinant[0] > 0 or determinant[0] < 0:
            x1 = determinant[1]/determinant[0]
            x2 = determinant[2]/determinant[0]
            x3 = determinant[3]/determinant[0]

            self.ui.label_10.setText("△ = " + str(determinant[0]))
            self.ui.label_11.setText("△1 = " + str(determinant[1]))
            self.ui.label_12.setText("△2 = " + str(determinant[2]))
            self.ui.label_13.setText("△3 = " + str(determinant[3]))
            self.ui.label_14.setText("x1 = " + str(x1))
            self.ui.label_15.setText("x2 = " + str(x2))
            self.ui.label_16.setText("x3 = " + str(x3))
        else:
            self.ui.label_10.setText("△= " + str(determinant[0]))
            self.ui.label_11.setText("△1 = ")
            self.ui.label_12.setText("△2 = ")
            self.ui.label_13.setText("△3 = ")
            self.ui.label_14.setText("x1 = ")
            self.ui.label_15.setText("x2 = ")
            self.ui.label_16.setText("x3 = ")


ui = WindowEquation()
# ui_2x2 = WindowMatrix2x2()
# ui_3x3 = WindowMatrix3x3()

# Run mainloop
sys.exit(app.exec_())
