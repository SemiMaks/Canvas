# Эта программа демонстрирует элемент интерфейса Canvas.

import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Создаём элемент интерфейса Canvas.
        self.canvas = tkinter.Canvas(self.main_window,
                                     width=200, height=200)

        point = (10, 10, 189, 10, 100, 189, 10, 10)
        self.canvas.create_line(point)

        # Нарисовать две прямые.
        self.canvas.create_line(0, 0, 199, 199, arrow=tkinter.LAST)
        self.canvas.create_line(199, 0, 0, 199, arrow=tkinter.FIRST)
        self.canvas.create_line(100, 0, 100, 200, arrow=tkinter.BOTH)
        self.canvas.create_line(50, 0, 50, 200, dash=(5, 2), fill='red', smooth=True, width=5)

        # Упаковать холст.
        self.canvas.pack()

        # Запускаем главный цикл.
        tkinter.mainloop()


# Создаём экземпляр класса.
my_gui = MyGUI()
