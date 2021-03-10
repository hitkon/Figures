#######################################################
# 
# Figure.py
# Python implementation of the Class Figure
# Generated by Enterprise Architect
# Created on:      08-����-2021 19:52:00
# Original author: tealh
# 
#######################################################


class Figure:
    # points = []
    # obj = []
    def __init__(self):
        self.line_color = "black"
        self.points = []
        self.obj = []
        self.id = None

    def draw(self, canvas):
        pass

    def get_line_color(self):
        return self.line_color

    def get_points(self):
        return self.points

    def move(self, delta, canvas):
        for i, p in enumerate(self.points):
            self.points[i] += delta
        canvas.move(self.id, delta.x, delta.y)

    def set_line_color(self, color):
        self.line_color = color

    def set_points(self, points):
        self.points = points

    def delete(self, canvas):
        for i in self.obj:
            canvas.delete(i)