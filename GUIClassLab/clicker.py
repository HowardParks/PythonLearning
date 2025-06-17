import tkinter as tk
from random import randint
gamestarted = False

def ticktok():
    global timer
    timer = timer + 1
    countup['text'] = str(timer)
    if len(numbers) > 0:
        window.after(1000, ticktok)


def clicked(event):
    global numbers, gamestarted
    if not gamestarted:
        gamestarted = True
        window.after(1000, ticktok)
    btn = int(event.widget['text'])
    if btn == numbers[0]:
        event.widget["state"] = tk.DISABLED
        del numbers[0]

window = tk.Tk()
window.title("Clicked")

numbers=[]
while len(numbers)<25:
    n = randint(0,999)
    if n not in numbers:
        numbers.append(n)

buttons = []
for brow in range(5):
    for bcolumn in range(5):
        index = brow*5 + bcolumn
        buttons.append(tk.Button(window,width=15,text=str(numbers[index])))
        buttons[index].grid(row=brow, column=bcolumn)
# Write your code here.
numbers.sort()
window.bind_all("<Button-1>", clicked)
timer = 0
countup = tk.Label(window, text=str(timer))
countup.grid(row=5, column=2)

window.mainloop()