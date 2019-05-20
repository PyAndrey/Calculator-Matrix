
from copy import copy
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as box

import numpy as np

from about_programm import *
from clear_function import *
from matrix import (matrix_determinant_2x2,
                    matrix_determinant_2x2_in_label,
                    matrix_3x3)


def bypass_list(list: list) -> list:
    """Преобразует элементы в int"""
    list1 = []
    for i in list:
        try:
            list1.append(int(i))
        except ValueError:
            box.showerror("Error", "Должны быть только цифры!")
            raise ValueError
    return list1


def calculate_matrix_2x2():
    """Calculation matrix"""
    s1 = input13.get()
    s2 = input14.get()
    s3 = input15.get()
    s4 = input16.get()
    # -------------------------#
    a1 = []
    a1.extend([s1, s2])
    a2 = []
    a2.extend([s3, s4])
    # --------------------------#
    try:
        a1: list = bypass_list(a1)
        a2: list = bypass_list(a2)
    except ValueError:
        return

    matrix = np.array([a1, a2])

    el1, el2, el3, el4 = matrix_determinant_2x2_in_label(matrix)

    res = matrix_determinant_2x2(matrix)

    stroka = "= {0} * {3} - {1} * {2} = {4}".format(el1, el2, el3, el4, res)

    if res is not None:
        Label(window, text=stroka).place(
            relx=.5, rely=.5, anchor="n", bordermode=INSIDE)


def matrix_2x2():
    """Поля для ввода чисел матрицы"""
    clear_grid(window)

    Label(window, text="|").place(relx=.37, rely=0.0, anchor="n",
                                  relheight=.1, relwidth=.1, bordermode=INSIDE)
    Label(window, text="|").place(relx=.37, rely=0.1, anchor="n",
                                  relheight=.1, relwidth=.1, bordermode=INSIDE)
    Label(window, text="|").place(relx=.63, rely=0.0, anchor="n",
                                  relheight=.1, relwidth=.1, bordermode=INSIDE)
    Label(window, text="|").place(relx=.63, rely=0.1, anchor="n",
                                  relheight=.1, relwidth=.1, bordermode=INSIDE)

    Label(window, text="=").place(relx=.66, rely=0.05, anchor="n",
                                  relheight=.1, relwidth=.05, bordermode=INSIDE)
    global input13
    input13 = Entry(window, justify=CENTER, width=10, borderwidth=5)
    input13.place(relx=.45, anchor="n", relheight=.1,
                  relwidth=.1, bordermode=INSIDE)

    global input14
    input14 = Entry(window, justify=CENTER, width=10, borderwidth=5)
    input14.place(relx=.55, anchor="n", relheight=.1,
                  relwidth=.1, bordermode=INSIDE)

    global input15
    input15 = Entry(window, justify=CENTER, width=10, borderwidth=5)
    input15.place(relx=.45, rely=0.1, anchor="n",
                  relheight=.1, relwidth=.1, bordermode=INSIDE)

    global input16
    input16 = Entry(window, justify=CENTER, width=10, borderwidth=5)
    input16.place(relx=.55, rely=0.1, anchor="n",
                  relheight=.1, relwidth=.1, bordermode=INSIDE)

    Button(window, text="Расчитать", command=calculate_matrix_2x2).place(
        relx=.5, rely=0.25, anchor="n", relheight=.15, relwidth=.2, bordermode=OUTSIDE)


def get_data(list: list) -> list:
    """Получает данные строк и сохраняет в список."""
    list = [input.get() for input in list]
    return list


def calculation_equetions():
    """Calculation equetions"""
    list = get_data(inputs)
    # -------------------------#
    a1 = []
    a1.extend([list[0], list[1], list[2], list[3]])
    a2 = []
    a2.extend([list[4], list[5], list[6], list[7]])
    a3 = []
    a3.extend([list[8], list[9], list[10], list[11]])
    try:
        a1: list = bypass_list(a1)
        a2: list = bypass_list(a2)
        a3: list = bypass_list(a3)
    except ValueError:
        return

    matrix = np.array([a1, a2, a3])

    determinant = []
    determinant.append(matrix_3x3(matrix))

    for i in range(3):
        list1, list2, list3 = a1.copy(), a2.copy(), a3.copy()

        list1[i] = list1[3]
        list2[i] = list2[3]
        list3[i] = list3[3]
        matrix = np.array([list1, list2, list3])

        determinant.append(matrix_3x3(matrix))

    if determinant[0] > 0 or determinant[0] < 0:
        x1 = determinant[1]/determinant[0]
        x2 = determinant[2]/determinant[0]
        x3 = determinant[3]/determinant[0]

        Label(window, text="△ = " + str(determinant[0])).grid(row=5,
                                                                   column=2, columnspan=5, sticky="s")
        Label(window, text="△1 = " + str(determinant[1])).grid(row=6,
                                                                   column=2, columnspan=5, sticky="s")
        Label(window, text="△2 = " + str(determinant[2])).grid(row=7,
                                                                   column=2, columnspan=5, sticky="s")
        Label(window, text="△3 = " + str(determinant[3])).grid(row=8,
                                                                  column=2, columnspan=5, sticky="s")

        Label(window, text="x1 = " + str(x1)).grid(row=9,
                                                   column=2, columnspan=5, sticky="s")
        Label(window, text="x2 = " + str(x2), width=50).grid(row=10,
                                                             column=2, columnspan=5, sticky="s")
        Label(window, text="x3 = " + str(x3)).grid(row=11,
                                                   column=2, columnspan=5, sticky="s")
    else:
        Label(window, text="Определитель равен 0").grid(
            row=5, column=2, columnspan=5, sticky="s")


def equation():
    """Поля для ввода чисел уравнений."""
    clear_place(window)

    Label(window, text="* x1 +", width=10).grid(row=1, column=2)
    Label(window, text="* x1 +", width=10).grid(row=2, column=2)
    Label(window, text="* x1 +", width=10).grid(row=3, column=2)
    Label(window, text="* x2 +").grid(row=1, column=4)
    Label(window, text="* x2 +").grid(row=2, column=4)
    Label(window, text="* x2 +").grid(row=3, column=4)
    Label(window, text="* x3 =", width=10).grid(row=1, column=6)
    Label(window, text="* x3 =", width=10).grid(row=2, column=6)
    Label(window, text="* x3 =", width=10).grid(row=3, column=6)

    # Inputs string
    global inputs
    inputs = []
    for x in range(1, 4):
        for j in range(1, 9, 2):
            input = Entry(window, justify=CENTER, width=10, borderwidth=5)
            input.grid(row=x, column=j)
            inputs.append(input)

    # calc button
    Button(window, text="Расчитать", command=calculation_equetions).grid(
        row=4, column=4, sticky=S)


# Window creating
window = Tk()
window.eval('tk::PlaceWindow %s center' %
            window.winfo_pathname(window.winfo_id()))
window.title("System of equeations")
window.geometry("510x280")
window.resizable(0, 0)
matrix_2x2()

# Добавляет меню вверху программы
mainmenu = Menu(window)
window.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть...")
filemenu.add_command(label="Новый")
filemenu.add_command(label="Сохранить...")
filemenu.add_command(label="Выход", command=window.quit)

wiewmenu = Menu(mainmenu, tearoff=0)
wiewmenu.add_command(label='Режим матрицы 2x2', command=matrix_2x2)
wiewmenu.add_command(label='Режим уравнения', command=equation)

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Помощь", command=help_window)
helpmenu.add_command(label="О программе", command=about_programm)

mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Режим", menu=wiewmenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)

window.mainloop()
