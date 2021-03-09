
import tkinter
from tkinter import colorchooser
from Interval import Interval

from tkinter import Tk, Frame, Menu, Button
from tkinter import LEFT, RIGHT, TOP, X, FLAT, RAISED


class ToolBar(Frame):
    def __init__(self, app):
        super().__init__(app)
        self.pack(side=RIGHT, fill=X)

        self.button_interval = tkinter.Button(self, text='Interval', command=FigureChooser(app, 'Interval'),
                                              width=20, height=1).grid(row=0, column=0, padx=23, pady=5, columnspan=2)
        self.button_ray = tkinter.Button(self, text='Ray', command=FigureChooser(app, 'Ray'),
                                         width=20, height=1).grid(row=1, column=0, padx=23, pady=5, columnspan=2)
        self.button_line = tkinter.Button(self, text='Line', command=FigureChooser(app, 'Line'),
                                          width=20, height=1).grid(row=2, column=0, padx=23, pady=5, columnspan=2)

        self.button_pace1 = tkinter.Button(self, text='', width=20, height=1, relief=tkinter.FLAT)\
            .grid(row=3, column=0, padx=23, pady=1, columnspan=2)

        self.button_rectangle = tkinter.Button(self, text='Rect', command=FigureChooser(app, 'Rect'),
                                          width=10, height=1).grid(row=4, column=0, padx=3, pady=5)
        self.button_rhomb = tkinter.Button(self, text='Rhomb', command=FigureChooser(app, 'Rhomb'),
                                          width=10, height=1).grid(row=4, column=1, padx=3, pady=5)
        self.button_triangle = tkinter.Button(self, text='Triangle', command=FigureChooser(app, 'Triangle'),
                                          width=10, height=1).grid(row=5, column=0, padx=3, pady=5)
        self.button_pentagon = tkinter.Button(self, text='Pentagon', command=FigureChooser(app, 'Pentagon'),
                                          width=10, height=1).grid(row=5, column=1, padx=3, pady=5)
        self.button_oval = tkinter.Button(self, text='Oval', command=FigureChooser(app, 'Oval'),
                                          width=10, height=1).grid(row=6, column=0, padx=3, pady=5)

        self.button_pace1 = tkinter.Button(self, text='', width=20, height=1, relief=tkinter.FLAT)\
            .grid(row=7, column=0, padx=23, pady=1, columnspan=2)

        self.button_Line_Color = tkinter.Button(self, text='Line Color', command=app.Linecolor, width=20, height=2)
        self.button_Line_Color.grid(row=8, column=0, padx=10, pady=10, columnspan=2)
        self.button_Fill_Color = tkinter.Button(self, text='Fill Color', command=app.Fillcolor, width=20, height=2)
        self.button_Fill_Color.grid(row=9, column=0, padx=10, pady=10, columnspan=2)
        self.button_move = tkinter.Button(self, text='Move', command=app.Fillcolor, width=20, height=2)
        self.button_move.grid(row=10, column=0, padx=10, pady=10, columnspan=2)

        self.button_pace1 = tkinter.Button(self, text='', width=20, height=1, relief=tkinter.FLAT)\
            .grid(row=11, column=0, padx=23, pady=1, columnspan=2)

        self.button_help = tkinter.Button(self, text='Help', command=app.Fillcolor, width=10, height=2)
        self.button_help.grid(row=12, column=1, padx=10, pady=10)






        #self.button_Rectangle = tkinter.Button(text='Rectangle', width=7, height=1).place(x=280, y=30)
        #self.button_Ellipse = tkinter.Button(text='Ellipse', width=7, height=1).place(x=350, y=30)


class FigureChooser:
    def __init__(self, app, figure_name):
        self.app = app
        self.figure_name = figure_name

    def __call__(self):
        self.app.choose_figure_name(self.figure_name)



