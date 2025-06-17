import tkinter as tk

phases = ((True,  False, False),
          (False,  False,  True),
          (False, True, False))

def lightem(phase):
    red,yellow,green = phase
    if red:
        canvas.itemconfig(redlight, fill="Red")
    else:
        canvas.itemconfig(redlight, fill="Black")
    if yellow:
        canvas.itemconfig(yellowlight, fill="Yellow")
    else:
        canvas.itemconfig(yellowlight, fill="Black")
    if green:
        canvas.itemconfig(greenlight, fill="Green")
    else:
        canvas.itemconfig(greenlight, fill="Black")

def nextphase():
    global cycle
    lightem(phases[cycle % len(phases)])
    cycle += 1

window = tk.Tk()
canvas = tk.Canvas(window, width=100, height=300, bg='DarkGray')
redlight = canvas.create_oval(5,5,95,95, fill="Black")
yellowlight = canvas.create_oval(5,105,95,195, fill="Black")
greenlight = canvas.create_oval(5,205,95,295, fill="Black")
canvas.pack()
nextbutton = tk.Button(window, text="Next", command=nextphase)
nextbutton.pack()
quitbutton = tk.Button(window, text="Quit", command=window.destroy)
quitbutton.pack()
cycle = 0
window.mainloop()
