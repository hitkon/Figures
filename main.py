import tkinter
from tkinter import colorchooser

from Point import Point
from Polygon import Polygon
from tool_bar import ToolBar

from Interval import Interval
from Ray import Ray
from Line import Line


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.canvas_cur_fig = None
        self.canvas_old_coords = None
        self.canvas_current_fill_color = 'black'
        self.canvas_current_line_color = 'black'
        self.geometry("1000x600")

        self.canvas = tkinter.Canvas(self, width=800, height=600, bg='white')
        self.init_canvas()

        self.tool_bar = ToolBar(self)

        self.Figures = []
        self.cur_fig_name = 'Line'
        self.cursor = 'Standard'

        self.LeftMousseButtonPressed = False
        self.bind('<Key-z>', self.delete_last_figure)

    def init_canvas(self):
        self.canvas.place(x=0, y=0)
        self.canvas.bind("<Button-1>", self.left_click)
        self.canvas.bind('<B1-Motion>', self.mouse_motion_with_left_button_pressed)
        self.canvas.bind('<ButtonRelease>', self.mouse_released)

    def figure_chooser(self, event):
        x1, y1, = self.canvas_old_coords
        if self.cur_fig_name == 'Line':
            return Line(x1, y1, event.x, event.y, self.canvas_current_line_color, self.canvas.winfo_width(),
                        self.canvas.winfo_height())
        if self.cur_fig_name == 'Ray':
            return Ray(x1, y1, event.x, event.y, self.canvas_current_line_color, self.canvas.winfo_width(),
                       self.canvas.winfo_height())
        if self.cur_fig_name == 'Interval':
            return Interval(x1, y1, event.x, event.y, self.canvas_current_line_color)
        if self.cur_fig_name == 'Polygon':
            return Polygon(x1, y1, event.x, event.y, self.canvas_current_line_color)

    def left_click(self, event):
        self.canvas_old_coords = event.x, event.y

    def mouse_motion_with_left_button_pressed(self, event):
        if self.cursor == 'Standard':
            if self.canvas_cur_fig:
                self.canvas_cur_fig.delete(self.canvas)
            self.canvas_cur_fig = self.figure_chooser(event)
            self.canvas_cur_fig.draw(self.canvas)
        if self.cursor == 'Move':
            item = self.canvas.find_closest(self.canvas_old_coords)
            #tag = self.canvas.itemcget("current", "tags")
            #if self.canvas_cur_fig:
            #    self.canvas_cur_fig.delete(self.canvas)
            delta = Point(event.x - self.canvas_old_coords[0], event.y - self.canvas_old_coords[1])
            self.canvas_old_coords = event.x, event.y
            self.canvas_cur_fig.move(delta)

            self.canvas_cur_fig.draw(self.canvas)

    def mouse_released(self, event):
        if self.cursor == 'Standard':
            if self.canvas_cur_fig:
                self.canvas_cur_fig.delete(self.canvas)
            self.Figures.append(self.figure_chooser(event))
            self.Figures[-1].draw(self.canvas)
        if self.cursor == 'Move':
            # if self.canvas.cur_fig:
            #    self.canvas.cur_fig.delete(self.canvas)
            self.Figures[-1].delete(self.canvas)
            self.Figures.pop()
            self.Figures.append(self.figure_chooser(event))
            self.Figures[-1].draw(self.canvas)

    def line_color(self):
        self.canvas_current_line_color = colorchooser.askcolor()[1]

    def choose_figure_name(self, figure_name):
        self.cur_fig_name = figure_name

    def fill_color(self):
        self.canvas_current_fill_color = colorchooser.askcolor()[1]
        # return my_color[1]

    def delete_last_figure(self):
        self.Figures[-1].delete(self.canvas)
        self.Figures.pop()
        # print('z-pressed')

    def move(self):
        self.cursor = 'Move'

    def clear(self):
        self.Figures.clear()
        self.canvas.delete("all")


if __name__ == '__main__':
    app = App()
    app.mainloop()

