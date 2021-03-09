# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter
from tkinter import colorchooser
from tool_bar import ToolBar

from Interval import Interval
from Ray import Ray
from Line import Line
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x600")

        self.canva = tkinter.Canvas(self, width=800, height=600, bg='white')
        self.init_canva()

        self.tool_bar = ToolBar(self)

        self.Figures = []
        self.cur_fig_name = 'Line'

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

    def figure_choser(self, event):
        x1, y1, = self.canva.old_coords
        if self.cur_fig_name == 'Line':
            return Line(x1, y1, event.x, event.y, self.canva.currentLineColor, self.canva.winfo_width(), self.canva.winfo_height())
        if self.cur_fig_name == 'Ray':
            return Ray(x1, y1, event.x, event.y, self.canva.currentLineColor, self.canva.winfo_width(), self.canva.winfo_height())
        if self.cur_fig_name == 'Interval':
            return Interval(x1, y1, event.x, event.y, self.canva.currentLineColor)

    def leftclick(self, event):
        self.canva.old_coords = event.x, event.y

    def mouseMotionWithLeftButtonPressed(self, event):
        x1, y1, = self.canva.old_coords
        if self.canva.cur_fig:
            self.canva.cur_fig.delete(self.canva)
        self.canva.cur_fig = self.figure_choser(event)
        self.canva.cur_fig.draw(self.canva)

    def mouseReleased(self, event):
        x1, y1, = self.canva.old_coords
        if self.canva.cur_fig:
            self.canva.cur_fig.delete(self.canva)
        self.Figures.append(self.figure_choser(event))
        self.Figures[-1].draw(self.canva)

    def Linecolor(self):
        self.canva.currentLineColor = colorchooser.askcolor()[1]

    def choose_figure_name(self, figure_name):
        self.cur_fig_name = figure_name

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
