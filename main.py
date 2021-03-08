# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter
from tkinter import colorchooser
from Interval import Interval

LeftMousseButtonPressed = False
Figures = []

def leftclick(event):
    canva.old_coords = event.x, event.y
    # a = Interval(event.x, event.y, event.x, event.y)
    #Figures.append(Interval(event.x, event.y, event.x, event.y))


def mouseMotionWithLeftButtonPressed(event):
    x1, y1, = canva.old_coords
    if canva.cur_fig:
        canva.cur_fig.delete(canva)
    canva.cur_fig = Interval(x1, y1, event.x, event.y, canva.currentLineColor)
    canva.cur_fig.draw(canva)
    #print ('Motion')

def mouseReleased(event):
    x1, y1, = canva.old_coords
    if canva.cur_fig:
        canva.cur_fig.delete(canva)
    Figures.append(Interval(x1, y1, event.x, event.y, canva.currentLineColor))
    Figures[-1].draw(canva)

def Linecolor():
    canva.currentLineColor = colorchooser.askcolor()[1]
    #print (currentLineColor)

def Fillcolor():
    canva.currentFillColor = colorchooser.askcolor()[1]
    # return my_color[1]

def deleteLastFigure(event):
    Figures[-1].delete(canva)
    Figures.pop()
    #print('z-pressed')

if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry("600x600")

    canva = tkinter.Canvas(root, width = 200, height= 400, bg = 'white')

    canva.old_coords = None
    canva.cur_fig = None

    canva.bind("<Button-1>", leftclick)
    canva.bind('<B1-Motion>', mouseMotionWithLeftButtonPressed)
    canva.bind('<ButtonRelease>', mouseReleased)
    root.bind('<Key-z>', deleteLastFigure)
    canva.place(x=0,y=0)



    button_Line_Color = tkinter.Button(text= 'Line Color', command=Linecolor, width = 7, height = 1)
    button_Line_Color.place(x=210,y=0)
    button_Fill_Color = tkinter.Button(text='Fill Color', command=Fillcolor, width=7, height=1)
    button_Fill_Color.place(x=280, y=0)

    button_Line = tkinter.Button(text = 'Line', width=7, height = 1).place(x = 210, y = 30)
    button_Rectangle = tkinter.Button(text='Rectangle', width=7, height=1).place(x=280, y=30)
    button_Ellipse = tkinter.Button(text='Ellipse', width=7, height=1).place(x=350, y=30)

    var = tkinter.IntVar()
    var.set(0)
    Line_RadioButton = tkinter.Radiobutton(text = 'Line', variable = var, value = 0).place(x=210, y = 60)
    Ray_RadioButton = tkinter.Radiobutton(text='Ray', variable=var, value=1).place(x=210, y = 90)
    Interval_RadioButton = tkinter.Radiobutton(text='Interval', variable=var, value=2).place(x=210, y = 120)


    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
