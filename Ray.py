#######################################################
# 
# Ray.py
# Python implementation of the Class Ray
# Generated by Enterprise Architect
# Created on:      08-����-2021 19:52:00
# Original author: tealh
# 
#######################################################
from Interval import Interval


class Ray(Interval):
    def __init__(self, x1, y1, x2, y2, color, width, height, tags):
        if x2 > x1:
            bufy = ((y1 - y2) * width * 10 + x1 * y2 - x2 * y1) / (x1 - x2)
            Interval.__init__(self, x1, y1, width * 10, bufy, color, tags)
        elif x1 == x2:
            pass
        else:
            bufy = ((y1 - y2) * width * (-10) + x1 * y2 - x2 * y1) / (x1 - x2)
            Interval.__init__(self, x1, y1, width * (-10), bufy, color, tags)
        if y2 > y1:
            bufx = ((x2 - x1) * height * 10 + x1 * y2 - x2 * y1) / (y2 - y1)
            Interval.__init__(self, x1, y1, bufx, height * 10, color, tags)
        elif y1 == y2:
            pass
        else:
            bufx = ((x2 - x1) * height * (-10) + x1 * y2 - x2 * y1) / (y2 - y1)
            Interval.__init__(self, x1, y1, bufx, height * (-10), color, tags)