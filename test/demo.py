# -*- coding: utf-8 -*-
import time

__author__ = 'l'
__date__ = '2018/5/14'
import numpy as np
import tkinter as tk

cav = np.zeros((10, 10), dtype=np.int)
cav[2][2] = 1
cav[3][3] = 2
window = tk.Tk()
window.title('my window')
window.geometry('1000x1000')
canvas = tk.Canvas(window, bg='white', height=1000, width=1000)
rect = None
for i in range(10):
    for j in range(10):
        if cav[i][j] == 1:
            x0 = (i - 1) * 100
            x1 = i * 100
            y0 = (j - 1) * 100
            y1 = j * 100
            rect = canvas.create_rectangle(x0, y0, x1, y1, fill='green')
canvas.pack()
for i in range(10):
    for j in range(10):
        if cav[i][j] == 2:
            x0 = (i - 1) * 100
            x1 = i * 100
            y0 = (j - 1) * 100
            y1 = j * 100
            rect = canvas.create_rectangle(x0, y0, x1, y1, fill='black')


def moveit():
    canvas.move(rect, 0, 2)


window.mainloop()
