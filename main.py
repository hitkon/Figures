# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter
from tkinter import colorchooser

from Interval import Interval

from tool_bar import ToolBar
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x600")

        self.canva = tkinter.Canvas(self, width=800, height=600, bg='white')
        self.init_canva()

        self.tool_bar = ToolBar(self)

        self.Figures = []
        self.current_figure_name = 'Interval'
        self.names_to_figures = {
            'Interval': Interval
        }

        self.LeftMousseButtonPressed = False
        self.bind('<Key-z>', self.deleteLastFigure)

    def init_canva(self):
        self.canva.place(x=0, y=0)
        self.canva.currentLineColor = 'black'
        self.canva.currentFillColor = 'black'
        self.canva.old_coords = None
        self.canva.cur_fig = None

        self.canva.bind("<Button-1>", self.leftclick)
        self.canva.bind('<B1-Motion>', self.mouseMotionWithLeftButtonPressed)
        self.canva.bind('<ButtonRelease>', self.mouseReleased)

    def leftclick(self, event):
        self.canva.old_coords = event.x, event.y
        # a = Interval(event.x, event.y, event.x, event.y)
        # Figures.append(Interval(event.x, event.y, event.x, event.y))

    def mouseMotionWithLeftButtonPressed(self, event):
        x1, y1, = self.canva.old_coords
        if self.canva.cur_fig:
            self.canva.cur_fig.delete(self.canva)
        cur_figure_class = self.names_to_figures[self.current_figure_name]
        self.canva.cur_fig = cur_figure_class(x1, y1, event.x, event.y, self.canva.currentLineColor)
        self.canva.cur_fig.draw(self.canva)
        # print ('Motion')

    def mouseReleased(self, event):
        x1, y1, = self.canva.old_coords
        if self.canva.cur_fig:
            self.canva.cur_fig.delete(self.canva)
        self.Figures.append(Interval(x1, y1, event.x, event.y, self.canva.currentLineColor))
        self.Figures[-1].draw(self.canva)

    def Linecolor(self):
        self.canva.currentLineColor = colorchooser.askcolor()[1]
        # print (currentLineColor)

    def choose_figure_name(self, figure_name):
        self.current_figure_name = figure_name

    def Fillcolor(self):
        self.canva.currentFillColor = colorchooser.askcolor()[1]
        # return my_color[1]

    def deleteLastFigure(self, event):
        self.Figures[-1].delete(self.canva)
        self.Figures.pop()
        # print('z-pressed')


if __name__ == '__main__':
    app = App()
    app.mainloop()
