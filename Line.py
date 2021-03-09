#######################################################
# 
# Line.py
# Python implementation of the Class Line
# Generated by Enterprise Architect
# Created on:      08-����-2021 19:52:00
# Original author: tealh
# 
#######################################################
from Interval import Interval
from Point import Point

class Line(Interval):
    def __init__(self, x1, y1, x2, y2, color, width, height):
        if x1 == x2:
            Interval.__init__(self, x1, 0, x1, height, color)
        elif y1 == y2:
            Interval.__init__(self, 0, y1, width, y1, color)
        else:
            points = []
            bufy = ((y1 - y2) * width + x1 * y2 - x2 * y1) / (x1 - x2)
            if bufy >= 0 and bufy <= height:
                points.append(Point(width, bufy))
            bufy = (x1 * y2 - x2 * y1) / (x1 - x2)
            if bufy >= 0 and bufy <= height:
                points.append(Point(0, bufy))
            bufx = ((x2 - x1) * height + x1 * y2 - x2 * y1) / (y2 - y1)
            if bufx >= 0 and bufx <= width:
                points.append(Point(bufx, height))
            bufx = (x1 * y2 - x2 * y1) / (y2 - y1)
            if bufx >= 0 and bufx <= width:
                points.append(Point(bufx, 0))
            Interval.__init__(self, points[0].get_x(), points[0].get_y(), points[-1].get_x(), points[-1].get_y(), color)