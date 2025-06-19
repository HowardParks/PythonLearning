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

def solved(xes, oes):
    solutions = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}]
    for who,sofar in {'X': xes, 'O': oes}.items():
        if any([win for win in solutions if win <= sofar]):
            return who
    return None


def clicked(event):
    global player, xes, oes
    print(event)
    index = event.widget.index
    if index in xes | oes:
       return
    if player == 0:
        drawx(event.widget)
        xes.add(index)
        event.widget.square = "X"
    else:
        drawo(event.widget)
        oes.add(index)
        event.widget.square = "O"
    print(f"{player} clicked {index}")
    player = 1 - player

def computermove():
    choice = random.randint(0,8)
    canvases[choice].event_generate('<1>', x=10, y=10)

def playgame():
    global player, oes, xes
    gameover = False
    while not gameover:
        if player == 0:
            computermove()
        winner = solved(xes, oes)
        if winner is not None:
            messagebox.showinfo(title="GameOver", message=f"{winner} wins!")
            gameover = True
        elif len(xes) + len(oes) == 9:
            messagebox.showinfo(title="GameOver", message="Cat's Game!")
            gameover = True

        window.update()

window=tk.Tk()
canvases = []
for row in range(3):
    for col in range(3):
        index = row*3 + col
        canvases.append(TicTac(window, index, bg="DarkGray",bd=2,height=30,width=30))
        canvases[index].grid(row=row, column=col)
        # canvases[index].bind('<1>', func=clicked)
window.bind_all('<1>', func=clicked)

xes = set(())
oes = set(())
player = 0
playgame()
window.destroy()
#window.mainloop()
