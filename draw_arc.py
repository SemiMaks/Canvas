# Эта программа чертит дугу на элементе Canvas.

import tkinter


class MyGUI:
    def __init__(self):
        # Создаём главное окно.
        self.main_window = tkinter.Tk()

        # Создаём элемент интерфейса Canvas.
        self.canvas = tkinter.Canvas(self.main_window,
                                     width=200, height=200)

        # Рисуем дугу.
        self.canvas.create_arc(10, 10, 190, 190, start=45, extent=30)
        self.canvas.create_arc(10, 10, 190, 190, start=180, extent=100, style=tkinter.ARC)
        self.canvas.create_arc(10, 10, 190, 190, start=90, extent=60, dash=(5,2), outline='red', fill='blue', width=5)
        self.canvas.create_arc(10, 10, 190, 190, start=300, extent=100, style=tkinter.CHORD)

        # Упаковываем холст.
        self.canvas.pack()

        # Запускаем главный цикл.
        tkinter.mainloop()


# Создаём экземпляр класса MyGUI.
my_gui = MyGUI()
