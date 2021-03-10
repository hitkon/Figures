import tkinter
from tkinter import colorchooser

from Point import Point
from tool_bar import ToolBar

from Interval import Interval
from Ray import Ray
from Line import Line

from Polygon import Polygon
from Ellipse import Ellipse




class App(tkinter.Tk):
    DEFAULT_WINDOW_MUL = 100

    def __init__(self):
        super().__init__()
        self.canvas_cur_fig = None
        self.canvas_old_coords = None
        self.canvas_current_fill_color = 'white'
        self.canvas_current_line_color = 'black'
        self.geometry("1000x600")

        self.canvas = tkinter.Canvas(self, width=800, height=600, bg='white')
        self.init_canvas()

        self.tool_bar = ToolBar(self)

        self.figures = []
        self.tags = {}
        self.cur_fig_name = 'Line'
        self.cursor = 'Standard'

        self.left_mouse_button_pressed = False
        self.bind('<Key-z>', self.delete_last_figure)
        self.bind('<KeyPress-Alt_L>', self.set_regular_on_alt_press)
        self.bind('<KeyRelease-Alt_L>', self.set_no_regular_on_alt_release)

        self.is_regular = False

    def init_canvas(self):
        self.canvas.place(x=0, y=0)
        self.canvas.bind("<Button-1>", self.left_click)
        self.canvas.bind('<B1-Motion>', self.mouse_motion_with_left_button_pressed)
        self.canvas.bind('<ButtonRelease>', self.mouse_released)

    def figure_chooser(self, event):
        x1, y1, = self.canvas_old_coords
        x1, y1, event.x, event.y = self.process_regular(x1, y1, event.x, event.y)
        max_tag = 0
        if self.tags:
            max_tag = max(self.tags.keys()) + 1

        if self.cur_fig_name == 'Line':
            self.tags[max_tag] = Line(x1, y1, event.x, event.y, self.canvas_current_line_color,
                                      self.canvas.winfo_width() * App.DEFAULT_WINDOW_MUL,
                                      self.canvas.winfo_height() * App.DEFAULT_WINDOW_MUL, max_tag)
            return self.tags[max_tag]
        if self.cur_fig_name == 'Ray':
            self.tags[max_tag] = Ray(x1, y1, event.x, event.y, self.canvas_current_line_color,
                                     self.canvas.winfo_width() * App.DEFAULT_WINDOW_MUL,
                                     self.canvas.winfo_height() * App.DEFAULT_WINDOW_MUL, max_tag)
            return self.tags[max_tag]
        if self.cur_fig_name == 'Interval':
            self.tags[max_tag] = Interval(x1, y1, event.x, event.y, self.canvas_current_line_color, max_tag)
            return self.tags[max_tag]
        if self.cur_fig_name == 'Polygon':
            self.tags[max_tag] = Polygon(x1, y1, event.x, event.y, self.canvas_current_line_color, max_tag)
            return self.tags[max_tag]
        if self.cur_fig_name == 'Ellipse':
            self.tags[max_tag] = Ellipse(x1, y1, event.x, event.y, self.canvas_current_line_color,
                                         self.canvas_current_fill_color, max_tag)
            return self.tags[max_tag]

    def left_click(self, event):
        self.canvas_old_coords = event.x, event.y

    def mouse_motion_with_left_button_pressed(self, event):
        if self.cursor == 'Standard':
            if self.canvas_cur_fig:
                self.canvas_cur_fig.delete(self.canvas)
            self.canvas_cur_fig = self.figure_chooser(event)
            self.canvas_cur_fig.draw(self.canvas)
        if self.cursor == 'Move':
            delta = Point(event.x - self.canvas_old_coords[0], event.y - self.canvas_old_coords[1])
            self.canvas_old_coords = event.x, event.y
            tag = self.canvas.itemcget("current", "tags")
            if tag != '':
                o = self.tags[int(tag.split(' ', 1)[0])]
                o.move(delta, self.canvas)

    def mouse_released(self, event):
        if self.cursor == 'Standard':
            if self.canvas_cur_fig:
                self.canvas_cur_fig.delete(self.canvas)
            self.figures.append(self.figure_chooser(event))
            self.figures[-1].draw(self.canvas)
        if self.cursor == 'Move':
            pass

    def line_color(self):
        self.canvas_current_line_color = colorchooser.askcolor()[1]

    def fill_color(self):
        self.canvas_current_fill_color = colorchooser.askcolor()[1]

    def choose_figure_name(self, figure_name):
        self.cur_fig_name = figure_name

    def delete_last_figure(self, event=None):
        self.figures[-1].delete(self.canvas)
        self.figures.pop()
        # print('z-pressed')

    def move(self):
        self.cursor = 'Move'

    def clear(self):
        self.figures.clear()
        self.canvas.delete("all")

    def set_regular_on_alt_press(self, event=None):
        self.is_regular = True

    def set_no_regular_on_alt_release(self, event=None):
        self.is_regular = False

    def process_regular(self, x1, y1, x2, y2):
        if self.is_regular:
            xw = x2 - x1
            yw = y2 - y1
            x2 = x1 + sign(xw) * min(abs(xw), abs(yw))
            y2 = y1 + sign(yw) * min(abs(xw), abs(yw))
        return x1, y1, x2, y2


def sign(x):
    return int((x > 0) - (x < 0))


if __name__ == '__main__':
    app = App()
    app.mainloop()
