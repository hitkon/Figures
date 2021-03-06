#######################################################
# 
# RegularPolygon.py
# Python implementation of the Class RegularPolygon
# Generated by Enterprise Architect
# Created on:      08-����-2021 19:52:00
# Original author: tealh
# 
#######################################################
from Polygon import Polygon
from Point import Point


class RegularPolygon(Polygon):
    def __init__(self, points, num_sides,  line_color, fill_color, tags):
        self.line_color = line_color
        self.fill_color = fill_color
        self.tags = tags
        self.id = None

        x1, y1, x2, y2 = tuple(points)
        if num_sides == 3:
            self.points = [Point(x1, y2), Point((x1 + x2) / 2, y1), Point(x2, y2)]
        if num_sides == 4:
            self.points = [Point(x1, y1), Point(x2, y1), Point(x2, y2), Point(x1, y2)]
        if num_sides == 5:
            dx = (x2 - x1) / 5
            dy = (y2 - y1) / 2.5
            self.points = [Point(x1 + dx, y2), Point(x1, y1 + dy), Point((x1 + x2) / 2, y1),
                            Point(x2, y1 + dy), Point(x2 - dx, y2)]

        Polygon.__init__(self, self.points,  line_color, fill_color, tags)

    def get_sides_num(self):
        pass

    def set_sides_num(self):
        pass
