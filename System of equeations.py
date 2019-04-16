#-------------Version Alpha 1.1.13----------------#

# imports
from copy import copy
from tkinter import *
from tkinter import filedialog as fd

import numpy as np

from determinant import *

# Functions


def about_programm():
    """About_the_programm"""
    window = Tk()
    window.title("About programm")
    window.geometry("510x260+700+400")
    window.resizable(0, 0)
    out1 = Label(
        window, text="Программа для расчета систем уравнений с тремя переменными")
    out1.pack()
    out2 = Label(window, text="Авторы")
    out2.pack()
    out3 = Label(window, text="Юзвук Андрей")
    out3.pack()
    out4 = Label(window, text="Яковлев Олег")
    out4.pack()


def help_window():
    window = Tk()
    window.title("About programm")
    window.geometry("510x260+700+400")
    window.resizable(0, 0)
    out1 = Label(
        window, text="Вводите поочередно цифры\n в специальные формы, \nпотом нажмите 'Расчитать'.")
    out1.pack()


def calc():
    """Calculation"""
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
    """ Matrix solving by Kramer method"""
    def bypass_list(list1: list) -> list:
        list2 = []
        for i in list1:
            try:
                list2.append(int(i))
            except ValueError:
                box.showerror("Error", "Должны быть только цифры!")
        return list2

    a1: list = bypass_list(a1)
    a2: list = bypass_list(a2)
    a3: list = bypass_list(a3)
    matrix = np.array([a1, a2, a3])

    determinant = []
    determinant.append(finding_determinant(matrix))

    for i in range(3):
        list1, list2, list3 = a1.copy(), a2.copy(), a3.copy()

        list1[i] = list1[3]
        list2[i] = list2[3]
        list3[i] = list3[3]
        matrix = np.array([list1, list2, list3])

        determinant.append(finding_determinant(matrix))

    if determinant[0] > 0 or determinant[0] < 0:
        x1 = determinant[1]/determinant[0]
        x2 = determinant[2]/determinant[0]
        x3 = determinant[3]/determinant[0]

        out1 = Label(window, text="x1 = " + str(x1))
        out1.grid(row=5, column=2, columnspan=5, sticky="s")
        out2 = Label(window, text="x2 = " + str(x2), width=50)
        out2.grid(row=6, column=2, columnspan=5, sticky="s")
        out3 = Label(window, text="x3 = " + str(x3))
        out3.grid(row=7, column=2, columnspan=5, sticky="s")
    else:
        answer = Tk()
        answer.title("Answers")
        answer.resizable(0, 0)
        out1 = Label(answer, text=determinant, width=150)
        out1.pack()


# Window creating
window = Tk()
window.eval('tk::PlaceWindow %s center' %
            window.winfo_pathname(window.winfo_id()))
window.title("System of equeations")
window.geometry("510x280")
window.resizable(0, 0)
# Inputs string
input1 = Entry(window, justify=CENTER, width=10, borderwidth=5)
input1.grid(row=1, column=1)

label1 = Label(window, text="* x1 +", width=10).grid(row=1, column=2)

input2 = Entry(window, justify=CENTER, width=10, borderwidth=5)
input2.grid(row=1, column=3)

label2 = Label(window, text="* x2 +").grid(row=1, column=4)

input3 = Entry(window, justify=CENTER, width=10, borderwidth=5)
input3.grid(row=1, column=5)

label3 = Label(window, text="* x3 =", width=10).grid(row=1, column=6)

input4 = Entry(window, justify=CENTER, width=10, borderwidth=5)
input4.grid(row=1, column=7)

input5 = Entry(window, justify=CENTER, width=10, borderwidth=5)
input5.grid(row=2, column=1)

label4 = Label(window, text="* x1 +", width=10).grid(row=2, column=2)

input6 = Entry(window, justify=CENTER, width=10, borderwidth=5)
input6.grid(row=2, column=3)

label5 = Label(window, text="* x2 +").grid(row=2, column=4)

input7 = Entry(window, justify=CENTER, width=10, borderwidth=5)
input7.grid(row=2, column=5)

label6 = Label(window, text="* x3 =", width=10).grid(row=2, column=6)

input8 = Entry(window, justify=CENTER, width=10, borderwidth=5)
input8.grid(row=2, column=7)

input9 = Entry(window, justify=CENTER, width=10, borderwidth=5)
input9.grid(row=3, column=1)

label7 = Label(window, text="* x1 +", width=10).grid(row=3, column=2)

input10 = Entry(window, justify=CENTER, width=10, borderwidth=5)
input10.grid(row=3, column=3)

label8 = Label(window, text="* x2 +").grid(row=3, column=4)

input11 = Entry(window, justify=CENTER, width=10, borderwidth=5)
input11.grid(row=3, column=5)

label9 = Label(window, text="* x3 =", width=10).grid(row=3, column=6)

input12 = Entry(window, justify=CENTER, width=10, borderwidth=5)
input12.grid(row=3, column=7)

# calc button
calc_button = Button(window, text="Расчитать", command=calc)
calc_button.grid(row=4, column=4, sticky=S)

# Добавляет меню вверху программы
mainmenu = Menu(window)
window.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть...")
filemenu.add_command(label="Новый")
filemenu.add_command(label="Сохранить...")
filemenu.add_command(label="Выход", command=window.quit)

wiewmenu = Menu(mainmenu, tearoff=0)
wiewmenu.add_command(label='Внешний вид')

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Помощь", command=help_window)
helpmenu.add_command(label="О программе", command=about_programm)

mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Вид", menu=wiewmenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)

window.mainloop()
