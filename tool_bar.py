import tkinter

from tkinter import Frame
from tkinter import RIGHT, X


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
        self.button_line = tkinter.Button(self, text='Polygonal Line', command=FigureChooser(app, 'Polygonal Line'),
                                          width=20, height=1).grid(row=3, column=0, padx=23, pady=5, columnspan=2)

        self.button_pace1 = tkinter.Button(self, text='', width=20, height=1, relief=tkinter.FLAT) \
            .grid(row=4, column=0, padx=23, pady=1, columnspan=2)

        self.button_rectangle = tkinter.Button(self, text='Rect', command=FigureChooser(app, 'Rect'),
                                               width=10, height=1).grid(row=5, column=0, padx=3, pady=5)
        self.button_rhombus = tkinter.Button(self, text='Rhombus', command=FigureChooser(app, 'Rhombus'),
                                             width=10, height=1).grid(row=5, column=1, padx=3, pady=5)
        self.button_triangle = tkinter.Button(self, text='Triangle', command=FigureChooser(app, 'Triangle'),
                                              width=10, height=1).grid(row=6, column=0, padx=3, pady=5)
        self.button_pentagon = tkinter.Button(self, text='Pentagon', command=FigureChooser(app, 'Pentagon'),
                                              width=10, height=1).grid(row=6, column=1, padx=3, pady=5)
        self.button_ellipse = tkinter.Button(self, text='Ellipse', command=FigureChooser(app, 'Ellipse'),
                                             width=10, height=1).grid(row=7, column=0, padx=3, pady=5)
        self.button_polygon = tkinter.Button(self, text='Polygon', command=FigureChooser(app, 'Polygon'),
                                             width=10, height=1).grid(row=7, column=1, padx=3, pady=5)

        self.button_pace1 = tkinter.Button(self, text='', width=20, height=1, relief=tkinter.FLAT) \
            .grid(row=8, column=0, padx=23, pady=1, columnspan=2)

        self.button_Line_Color = tkinter.Button(self, text='Line Color', command=app.line_color, width=20, height=2)
        self.button_Line_Color.grid(row=9, column=0, padx=10, pady=2, columnspan=2)
        self.button_Fill_Color = tkinter.Button(self, text='Fill Color', command=app.fill_color, width=20, height=2)
        self.button_Fill_Color.grid(row=10, column=0, padx=10, pady=2, columnspan=2)
        self.button_move = tkinter.Button(self, text='Move', command=app.move, width=20, height=2)
        self.button_move.grid(row=11, column=0, padx=10, pady=2, columnspan=2)
        self.button_clear = tkinter.Button(self, text='Clear', command=app.clear, width=20, height=2)
        self.button_clear.grid(row=12, column=0, padx=10, pady=2, columnspan=2)

        self.button_pace1 = tkinter.Button(self, text='', width=20, height=1, relief=tkinter.FLAT) \
            .grid(row=13, column=0, padx=23, pady=1, columnspan=2)

        self.button_help = tkinter.Button(self, text='Help', command=app.fill_color, width=10, height=2)
        self.button_help.grid(row=14, column=1, padx=10, pady=1)


class FigureChooser:
    def __init__(self, app, figure_name):
        self.app = app
        self.figure_name = figure_name

    def __call__(self):
        self.app.cursor = 'Standard'
        self.app.choose_figure_name(self.figure_name)
