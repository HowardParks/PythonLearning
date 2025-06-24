import tkinter as tk
from functools import partial
# need to keep the float version of current

def isfloat(num):
    return num.replace('.','').replace('-','').isnumeric()

def click(key):
    global entryvar, register, pending
    current = entryvar.get()
    result = current
    if key in numbers:
        if current in ops or (current.isnumeric() and  float(current) == 0):
            result = key
        else:
            if len(result) < 10:
                result = current + key
    elif key == 'C':
        result = '0'
    elif key in ops:
        register = float(current)
        result = key
        pending = key
    elif key == '=':
        if  pending == '+':
            result = str(register + float(current))
        if  pending == '-':
            result = str(register - float(current))
        if  pending == '*':
            result = str(register * float(current))
        if  pending == '/':
            if float(current) == 0.0:
                pending = ''
                result = str(register)
            else:
                result = str(register / float(current))
        if 'e-' in result:
            result = f"{float(result):.10f}"
        register = float(result)
        pending = ''
        if result.endswith(".0") and result != '.0':
            result = result.replace(".0", "")
        if result.endswith('.') and result != '.':
            result = result.replace(",", "")
    elif key == '.':
        if current.isnumeric():
            if len(result) < 10:
                result = current + key
        else:
            result = key
    elif key == '+/-':
        result = str(float(current)*-1)
    else:
        result = key
    if len(result) > 10:
        result = result.ljust(10,'0')[:10]
    entryvar.set(result)
window = tk.Tk()
window.geometry("250x150")
window.title("Calculator")

entryvar = tk.StringVar()
entryvar.set('0')
display = tk.Entry(window, bg="WHITE", fg="BLACK", justify=tk.RIGHT, textvariable=entryvar, width=10, font=('Courier New', 12))
display.grid(row=1,column=1,columnspan=5)

numbers = {}
buttons =  {}
engage = {}

val = '0'
numbers[val] = tk.Button(window, text=val, bg="LightGray", command=partial(click,val), padx=1, width=5)
numbers[val].grid(row=5, column=1)
for row in [4,3,2]:
    for col in [1,2,3]:
        val = str(int(val) + 1)
        numbers[val] = tk.Button(window, text=val, bg="LightGray", command=partial(click,val), padx=1, width=5)
        numbers[val].grid(row=row, column=col)

ops = {'+': (2, 5), '-': (3, 5), '*': (4, 5), '/': (5, 5)}
for p in ops:
    buttons[p] = tk.Button(window, text=p, bg="LightGray", command=partial(click,p), padx=1, width=5)
    buttons[p].grid(row=ops[p][0], column=ops[p][1] )


other ={'=':(4,4),'+/-':(5,4),'C':(5,2),'.':(5,3)}
for p in other:
    buttons[p] = tk.Button(window, text=p, bg="LightGray", command=partial(click,p), padx=1, width=5)
    buttons[p].grid(row=other[p][0], column=other[p][1] )

register = 0.0
pending = None
window.mainloop()
