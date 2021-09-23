# Эта программа рисует прямоугольник на элементе Canvas.

import tkinter


class MyGUI:
    def __init__(self):
        # Создаём главное окно.
        self.main_window = tkinter.Tk()

        # Создаём элемент интерфейса Canvas
        self.canvas = tkinter.Canvas(self.main_window,
                                     width=200, heigh=200)

        # Рисуем прямоугольник.
        self.canvas.create_rectangle(20, 20, 180, 180)
        self.canvas.create_rectangle(40, 40, 160, 160, dash=(5, 2))
        self.canvas.create_rectangle(60, 60, 140, 140, outline='green')
        self.canvas.create_rectangle(80, 80, 120, 120, outline='red', width=3)
        self.canvas.create_rectangle(90, 90, 110, 110, outline='blue', fill='yellow')

        # Упаковываем холст.
        self.canvas.pack()

        # Запускаем главный цикл.
        tkinter.mainloop()


# Создаём экземпляр класса MyGUI.
my_guy = MyGUI()
