import tkinter as tk
import tkinter.messagebox as messagebox
import random

class TicTac(tk.Canvas):
    def __init__(self, parent, index, **kwargs):
        super().__init__(parent, **kwargs)
        self.index = index
        self.square = ''

def drawx(c):
    c.create_line(7,7,29,29,fill='Red',width=3)
    c.create_line(29,7,7,29,fill='Red',width=3)

def drawo(c):
    c.create_oval(7,7,29,29,outline='Green',width=3)

def solved(player, sofar):
    solutions = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}]
    which={0:'X', 1:'O'}
    if len(sofar) >= 3:
        for solution in solutions:
            if solution <= sofar:
                messagebox.showinfo(title="GameOver",message=f"{which[player]} wins!")
                window.destroy()

def clicked(event):
    global player, window, xes, oes
    try:
        print(f"Canvas {event.widget.index} clicked")
        if event.widget.index in xes | oes:
            return
    except AttributeError:
        return
    if player == 0:
        drawx(event.widget)
        xes.add(event.widget.index)
        event.widget.square = "X"
        solved(player,xes)
    else:
        drawo(event.widget)
        oes.add(event.widget.index)
        event.widget.square = "O"
        solved(player,oes)
    player = 1 - player

def computermove():
    while True:
        choice = random.randint(0,8)
        if canvases[choice].square == '':
            break
    canvases[choice].event_generate('<1>', x=10, y=10)

def playgame():
    global xes, oes, player
    print('Game started')
    while len(xes) + len(oes) < 9:
        computermove()
        messagebox.showinfo(message="Your turn!")
    messagebox.showinfo(title="GameOver", message="Cat's Game!")
    window.destroy()

window=tk.Tk()
canvases = []
for row in range(3):
    for col in range(3):
        index = row*3 + col
        canvases.append(TicTac(window, index, bg="DarkGray",bd=2,height=30,width=30))
        canvases[index].grid(row=row, column=col)
        canvases[index].bind('<1>', func=clicked)
#window.bind_all('<1>', func=clicked)
starter = tk.Button(text="Start", command=playgame)
starter.grid(row=3,column=1)

xes = set(())
oes = set(())
player = 0

window.mainloop()

