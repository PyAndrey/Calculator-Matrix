#-------------Version Alpha 1.4----------------#

from copy import copy
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as box

import numpy as np

from matrix import (matrix_determinant_second_order,
                    matrix_determinant_three_order,
                    matrix_determinant_second_order_in_label)


def about_programm():
    window = Tk()
    window.title("About programm")
    window.geometry("510x260+700+400")
    window.resizable(0, 0)
    Label(window, text="Программа для расчета систем уравнений с тремя переменными и матрицы").pack()
    Label(window, text="Авторы").pack()
    Label(window, text="Юзвук Андрей").pack()
    Label(window, text="Яковлев Олег").pack()


def help_window():
    window = Tk()
    window.title("Help programm")
    window.geometry("510x260+700+400")
    window.resizable(0, 0)
    Label(window, text="Вводите поочередно цифры\n в специальные формы, \nпотом нажмите 'Расчитать'.").pack()


def bypass_list(list1: list) -> list:
    """Преобразует элементы в int"""
    list2 = []
    for i in list1:
        try:
            list2.append(int(i))
        except ValueError:
            box.showerror("Error", "Должны быть только цифры!")
            raise ValueError
    return list2


def clear_grid():
    """Очищает окно от grid"""
    list = window.grid_slaves()
    for l in list:
        l.destroy()


def clear_place():
    """Очищает окно от place"""
    list = window.place_slaves()
    for l in list:
        l.destroy()


def calculate_matrix_second_order():
    """Calculation matrix"""
    s1 = input13.get()
    s2 = input14.get()
    s3 = input15.get()
    s4 = input16.get()
    #-------------------------#
    a1 = []
    a1.extend([s1, s2])
    a2 = []
    a2.extend([s3, s4])
    #--------------------------#
    try:
        a1: list = bypass_list(a1)
        a2: list = bypass_list(a2)
    except ValueError:
        return

    matrix = np.array([a1, a2])

    el1, el2, el3, el4 = matrix_determinant_second_order_in_label(matrix)

    res = matrix_determinant_second_order(matrix)

    stroka = "= {0} * {3} - {1} * {2} = {4}".format(el1, el2, el3, el4, res)

    if res != None:
        Label(window, text=stroka).place(
            relx=.5, rely=.5, anchor="n", bordermode=INSIDE)


def matrix_2x2():
    """Поля для ввода чисел матрицы"""
    clear_grid()

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
    input13.place(relx=.45, rely=0.0, anchor="n", relheight=.1,
                  relwidth=.1, bordermode=INSIDE)

    global input14
    input14 = Entry(window, justify=CENTER, width=10, borderwidth=5)
    input14.place(relx=.55, rely=0.0, anchor="n", relheight=.1,
                  relwidth=.1, bordermode=INSIDE)

    global input15
    input15 = Entry(window, justify=CENTER, width=10, borderwidth=5)
    input15.place(relx=.45, rely=0.1, anchor="n", relheight=.1,
                  relwidth=.1, bordermode=INSIDE)

    global input16
    input16 = Entry(window, justify=CENTER, width=10, borderwidth=5)
    input16.place(relx=.55, rely=0.1, anchor="n", relheight=.1,
                  relwidth=.1, bordermode=INSIDE)

    Button(window, text="Расчитать", command=calculate_matrix_second_order).place(
        relx=.5, rely=0.25, anchor="n", relheight=.15, relwidth=.2, bordermode=OUTSIDE)


def calculation_equetions():
    """Calculation equetions"""
    s1 = input1.get()
    s2 = input2.get()
    s3 = input3.get()
    s4 = input4.get()
    s5 = input5.get()
    s6 = input6.get()
    s7 = input7.get()
    s8 = input8.get()
    s9 = input9.get()
    s10 = input10.get()
    s11 = input11.get()
    s12 = input12.get()
    #-------------------------#
    a1 = []
    a1.extend([s1, s2, s3, s4])
    a2 = []
    a2.extend([s5, s6, s7, s8])
    a3 = []
    a3.extend([s9, s10, s11, s12])
    #--------------------------#
    try:
        a1: list = bypass_list(a1)
        a2: list = bypass_list(a2)
        a3: list = bypass_list(a3)
    except ValueError:
        return

    matrix = np.array([a1, a2, a3])

    determinant = []
    determinant.append(matrix_determinant_three_order(matrix))

    for i in range(3):
        list1, list2, list3 = a1.copy(), a2.copy(), a3.copy()

        list1[i] = list1[3]
        list2[i] = list2[3]
        list3[i] = list3[3]
        matrix = np.array([list1, list2, list3])

        determinant.append(matrix_determinant_three_order(matrix))

    if determinant[0] > 0 or determinant[0] < 0:
        x1 = determinant[1]/determinant[0]
        x2 = determinant[2]/determinant[0]
        x3 = determinant[3]/determinant[0]

        Label(window, text="x1 = " + str(x1)).grid(row=5,
                                                   column=2, columnspan=5, sticky="s")
        Label(window, text="x2 = " + str(x2), width=50).grid(row=6,
                                                             column=2, columnspan=5, sticky="s")
        Label(window, text="x3 = " + str(x3)).grid(row=7,
                                                   column=2, columnspan=5, sticky="s")
    else:
        answer = Tk()
        answer.title("Answers")
        answer.resizable(0, 0)
        Label(answer, text=determinant, width=150).pack()


def equation():
    """Поля для ввода чисел уравнений"""
    clear_place()

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
    global input1
    input1 = Entry(window, justify=CENTER, width=10, borderwidth=5)
    input1.grid(row=1, column=1)

    global input2
    input2 = Entry(window, justify=CENTER, width=10, borderwidth=5)
    input2.grid(row=1, column=3)

    global input3
    input3 = Entry(window, justify=CENTER, width=10, borderwidth=5)
    input3.grid(row=1, column=5)

    global input4
    input4 = Entry(window, justify=CENTER, width=10, borderwidth=5)
    input4.grid(row=1, column=7)

    global input5
    input5 = Entry(window, justify=CENTER, width=10, borderwidth=5)
    input5.grid(row=2, column=1)

    global input6
    input6 = Entry(window, justify=CENTER, width=10, borderwidth=5)
    input6.grid(row=2, column=3)

    global input7
    input7 = Entry(window, justify=CENTER, width=10, borderwidth=5)
    input7.grid(row=2, column=5)

    global input8
    input8 = Entry(window, justify=CENTER, width=10, borderwidth=5)
    input8.grid(row=2, column=7)

    global input9
    input9 = Entry(window, justify=CENTER, width=10, borderwidth=5)
    input9.grid(row=3, column=1)

    global input10
    input10 = Entry(window, justify=CENTER, width=10, borderwidth=5)
    input10.grid(row=3, column=3)

    global input11
    input11 = Entry(window, justify=CENTER, width=10, borderwidth=5)
    input11.grid(row=3, column=5)

    global input12
    input12 = Entry(window, justify=CENTER, width=10, borderwidth=5)
    input12.grid(row=3, column=7)

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
equation()

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
