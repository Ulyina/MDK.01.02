import tkinter as tk
from tkinter import Entry, Button, Label, Text
from sympy import symbols, sqrt, exp
import matplotlib.pyplot as plt

# Функция для вычисления значения функции y
def calculate_y(x, a, b):
    y = 2 * sqrt(5 * x - 9) / (7.5 * a * b + 18) + exp(2 * x + 0.5 / a)
    return y

# Функция для построения таблицы значений функции и вывода порядка выполнения операций
def build_table():
    try:
        xmin = float(entry_xmin.get())
        xmax = float(entry_xmax.get())
        dx = float(entry_dx.get())
        a = float(entry_a.get())
        b = float(entry_b.get())

        # Очистить текстовое поле перед добавлением новых значений
        output_text.delete(1.0, END)

        x_values = []
        y_values = []

        x = xmin
        while x <= xmax:
            y = calculate_y(x, a, b)
            x_values.append(x)
            y_values.append(y)
            output_text.insert(END, f"x = {x:.2f}, y = {y:.2f}\n")
            x += dx

        # Построение графика
        plt.plot(x_values, y_values)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('График функции y = 2√(5x-9) / (7.5ab+18) + e^(2x+0.5/a)')
        plt.grid(True)
        plt.show()
    except ValueError:
        output_text.insert(END, "Ошибка: Некорректный ввод.\n")

# Создание главного окна
root = tk.Tk()
root.title("Таблица значений функции")

# Создание и размещение элементов на форме
entry_xmin = Entry(root)
entry_xmax = Entry(root)
entry_dx = Entry(root)
entry_a = Entry(root)
entry_b = Entry(root)
label_xmin = Label(root, text="Введите xmin:")
label_xmax = Label(root, text="Введите xmax:")
label_dx = Label(root, text="Введите dx:")
label_a = Label(root, text="Введите a:")
label_b = Label(root, text="Введите b:")
button_plot = Button(root, text="Построить таблицу", command=build_table)

# Создание текстового поля для вывода таблицы значений
output_text = Text(root, height=15, width=40)
output_text.config(state="normal")  # Разрешаем редактирование текстового поля

# Загрузка изображения и создание объекта PhotoImage
image = tk.PhotoImage(file="graph2.png")
image_label = tk.Label(root, image=image)
image_label.photo = image

label_xmin.pack()
entry_xmin.pack()
label_xmax.pack()
entry_xmax.pack()
label_dx.pack()
entry_dx.pack()
label_a.pack()
entry_a.pack()
label_b.pack()
entry_b.pack()
button_plot.pack()
output_text.pack()
image_label.pack()

root.mainloop()
