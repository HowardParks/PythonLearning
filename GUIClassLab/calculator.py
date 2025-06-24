import tkinter as tk
from tkinter import messagebox

def doTheMath():
    global first, second, switch
    intmath = True
    arg1 = first.get()
    arg2 = second.get()
    operation = switch.get()
    try:
        if '.' in arg1:
            arg1 = float(arg1)
            intmath = False
        else:
            arg1 = int(arg1)
        if '.' in arg2:
            arg2 = float(arg2)
            intmath = False
        else:
            arg2 = int(arg2)
    except ValueError:
        tk.messagebox.showerror("Gah!", "Invalid Inputs")
        return
    if operation == 0:
        result=arg1 + arg2
    elif operation == 1:
        result = arg1 - arg2
    elif operation == 2:
        result = arg1 * arg2
    elif operation == 3:
        if arg2 == 0:
            tk.messagebox.showerror('Huh?',"I don't know what to do with this")
            return
        result = arg1/arg2
    if intmath:
        result = int(result)
    tk.messagebox.showinfo('Got it?',str(result))

# Write your code here.
window = tk.Tk()
window.title('Calculator')

switch = tk.IntVar()
switch.set(1)

first = tk.Entry(window, width=30)
first.grid(row=2,column=1,rowspan=2,sticky="")
second = tk.Entry(window,width=30)
second.grid(row=2,column=3,rowspan=2,sticky="")

plusbutton = tk.Radiobutton(window, text="+", variable=switch, value=0)
plusbutton.grid(row=1,column=2)
minusbutton = tk.Radiobutton(window, text="-", variable=switch, value=1)
minusbutton.grid(row=2,column=2)
timesbutton = tk.Radiobutton(window, text="*", variable=switch, value=2)
timesbutton.grid(row=3,column=2)
dividebutton = tk.Radiobutton(window, text="/", variable=switch, value=3)
dividebutton.grid(row=4,column=2)

evaluate = tk.Button(window, text='Evaluate', command=doTheMath)
evaluate.grid(row=5,column=2)

window.mainloop()
