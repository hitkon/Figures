#######################################################
# 
# PolygonalLine.py
# Python implementation of the Class PolygonalLine
# Generated by Enterprise Architect
# Created on:      08-����-2021 19:52:00
# Original author: tealh
# 
#######################################################
from OneDim import OneDim
from Interval import Interval
from Point import Point

class PolygonalLine(OneDim):
    def __init__(self, _points, x, y, color, tag):
        OneDim.__init__(self)
        self.points = _points
        self.points2 = []
        for i in self.points:
            self.points2.append(i.x)
            self.points2.append(i.y)
        self.points2.append(x)
        self.points2.append(y)

        self.points.append(Point(x, y))

        self.line_color = color
        self.tags = tag
        self.id = None

    def draw(self, canvas):
        self.id = canvas.create_line(self.points2,
                                     width=3, fill=self.line_color, tags=(self.tags,))

        self.points.pop()
        self.points2.pop()#WTF
        self.points2.pop()

        self.obj.append(self.id)