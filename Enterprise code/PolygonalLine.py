#######################################################
# 
# PolygonalLine.py
# Python implementation of the Class PolygonalLine
# Generated by Enterprise Architect
# Created on:      03-����-2021 9:28:12
# Original author: tealh
# 
#######################################################
import OneDim
import Interval
from OneDim import OneDim
from Interval import Interval

class PolygonalLine(OneDim):
<<<<<<< Updated upstream:Enterprise code/PolygonalLine.py
    m_Interval= Interval()
=======
    def __init__(self, points, color, tag):
        self.points = points
        self.obj = []
        self.line_color = color
        self.tag = tag
        self.id = None
    def draw(self, canvas):
        #for i in range(len(self.points)-1):
        self.obj.append(canvas.create_line(self.points[0].get_x(), self.points[0].get_y(),self.points[-1].get_x(), self.points[-1].get_y(), width=3, fill=self.line_color, tags=(self.tags,)))


>>>>>>> Stashed changes:PolygonalLine.py
