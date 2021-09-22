# Эта программа демонстрирует элемент интерфейса Canvas.

import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Создаём элемент интерфейса Canvas.
        self.canvas = tkinter.Canvas(self.main_window,
                                     width=200, height=200)

        # Нарисовать две прямые.
        self.canvas.create_line(0, 0, 199, 199)
        self.canvas.create_line(199, 0, 0, 199)

        # Упаковать холст.
        self.canvas.pack()

        # Запускаем главный цикл.
        tkinter.mainloop()


# Создаём экземпляр класса.
my_gui = MyGUI()
