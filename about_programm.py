from tkinter import *


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