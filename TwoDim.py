#######################################################
# 
# TwoDim.py
# Python implementation of the Class TwoDim
# Generated by Enterprise Architect
# Created on:      08-����-2021 19:52:00
# Original author: tealh
# 
#######################################################
from Figure import Figure


class TwoDim(Figure):
    def __init__(self):
        Figure.__init__(self)
        self.fill_color = "white"

    def fill(self):
        pass

    def get_fill_color(self):
        return self.fill_color

    def set_fill_color(self, color):
        self.fill_color = color
