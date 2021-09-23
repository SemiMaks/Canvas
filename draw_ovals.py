# Эта прграмма чертит овал на элементах Canvas.

import tkinter


class MyGUI:
    def __init__(self):
        # Создаём главное окно.
        self.main_window = tkinter.Tk()

        # Создаём элемент интерфейса Canvas.
        self.canvas = tkinter.Canvas(self.main_window,
                                     width=200, height=200)

        # Нарисовать два овала.
        self.canvas.create_oval(20, 20, 160, 120, widt=5)
        self.canvas.create_oval(40, 40, 140, 100, dash=(5, 2), outline='red')
        self.canvas.create_oval(60, 60, 120, 80, fill='green', outline='blue')

        # Упаковываем холст.
        self.canvas.pack()

        # Запускаем главный цикл.
        tkinter.mainloop()


# Создаем экземпляр класса MyGUI.
my_gui = MyGUI()
