# Эта программ чертит многоугольник на элементе Canvas.
import tkinter


class MyGUI:
    def __init__(self):
        # Создаём главное окно.
        self.main_window = tkinter.Tk()

        # Создать элемент интерфейса Canvas.
        self.canvas = tkinter.Canvas(self.main_window,
                                     width=160, height=160)

        # Чертим многоугольник.
        self.canvas.create_polygon(60, 20, 100, 20, 140, 60, 140, 100,
                                   100, 140, 60, 140, 20, 100, 20, 60)

        # Упаковываем холст.
        self.canvas.pack()

        # Запускаем главный цикл.
        tkinter.mainloop()


# Создаём экземпляр класса MyGUI.
my_gui = MyGUI()
