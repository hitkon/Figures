#######################################################
# 
# Interval.py
# Python implementation of the Class Interval
# Generated by Enterprise Architect
# Created on:      08-����-2021 19:52:00
# Original author: tealh
# 
#######################################################
from OneDim import OneDim
from Point import Point


class Interval(OneDim):
    def __init__(self, x1, y1, x2, y2, color):
        OneDim.__init__(self)
        self.line_color = color
        self.points.append(Point(x1, y1))
        self.points.append(Point(x2, y2))

    def draw(self, canvas):
        self.obj.append(canvas.create_line(self.points[0].get_x(), self.points[0].get_y(),
                                           self.points[-1].get_x(), self.points[-1].get_y(),
                                           width=3, fill=self.line_color))

    def move(self, delta, canvas, tag):
        for i, p in enumerate(self.points):
            self.points[i] += delta
        self.canvas.move(tag, self.points[0], self.points[1])

    # def left_click(self, event):
    #     self.points.append(Point(event.x, event.y))
    #     self.points.append(Point(event.x, event.y))
    #
    # def mouseMotionWithLeftButtonPressed(self, event):
    #     self.delete(self.canvas)
    #     self.points[-1].point_change(event.x, event.y)
    #     self.draw(self.canvas)
    #     # print ('Motion')
