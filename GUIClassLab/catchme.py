import tkinter as tk
import random
from math import sqrt

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**.5

def jump(blah):
    global oldx, oldy
    newx=oldx
    newy=oldy
    while distance(oldx, oldy, newx, newy) < 75:
        newx = random.randint(25,450)
        newy = random.randint(25,450)
    button.place(x=newx, y=newy)
    oldx = newx
    oldy = newy

window = tk.Tk()
window.title("Catch Me!")
window.geometry("500x500")

oldx=250
oldy=250
button = tk.Button(window, text="Catch me!")
button.place(x=oldx,y=oldy)
button.bind("<Enter>",jump)

window.mainloop()
