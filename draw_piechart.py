# Эта программа чертит круговую диаграмму на элементе Canvas.

import tkinter


class MyGUI:
    def __init__(self):
        self.__CANVAS_WIDTH = 320
        self.__CANVAS_HEIGHT = 240
        self.__X1 = 60
        self.__Y1 = 20
        self.__X2 = 260
        self.__Y2 = 220
        self.__PIE1_START = 0
        self.__PIE1_WIDTH = 45
        self.__PIE2_START = 45
        self.__PIE2_WIDTH = 90
        self.__PIE3_START = 135
        self.__PIE3_WIDTH = 120
        self.__PIE4_START = 255
        self.__PIE4_WIDTH = 105

        # Создаём главное окно.
        self.main_window = tkinter.Tk()

        # Создаём элемент интерфейса Canvas.
        self.canvas = tkinter.Canvas(self.main_window,
                                     width=self.__CANVAS_WIDTH,
                                     height=self.__CANVAS_HEIGHT)

        # Чертим сектор 1.
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, self.__Y2,
                               start=self.__PIE1_START, extent=self.__PIE1_WIDTH,
                               fill='green')

        # Чертим сектор 2.
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, self.__Y2,
                               start=self.__PIE2_START, extent=self.__PIE2_WIDTH,
                               fill='black')

        # Чертим сектор 3.
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, self.__Y2,
                               start=self.__PIE3_START, extent=self.__PIE3_WIDTH,
                               fill='red')

        # Чертим сектор 4.
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, self.__Y2,
                               start=self.__PIE4_START, extent=self.__PIE4_WIDTH,
                               fill='yellow')

        # Упаковываем холст.
        self.canvas.pack()

        # Запускаем главный цикл.
        tkinter.mainloop()


# Создаём экземпляр класса MyGUI.
my_gui = MyGUI()
