import tkinter as tk
from PIL import Image
from PIL import EpsImagePlugin
EpsImagePlugin.gs_windows_binary =  r'C:\Program Files\gs\gs10.05.1\bin\gswin64c'

window = tk.Tk()
canvasb = tk.Canvas(window, bg='DarkGray', bd=2, height=30, width=30)
canvasb.pack()
canvasx = tk.Canvas(window, bg='DarkGray', bd=2, height=30, width=30)
canvasx.pack()
canvaso = tk.Canvas(window, bg='DarkGray', bd=2, height=30, width=30)
canvaso.pack()

canvasx.create_line(7,7,29,29,fill='Red',width=3)
canvasx.create_line(29,7,7,29,fill='Red',width=3)

canvaso.create_oval(7,7,29,29,outline='Green',width=3)

canvasb.postscript(file='tictactoe_b.eps')
canvasx.postscript(file='tictactoe_x.eps')
canvaso.postscript(file='tictactoe_o.eps')

img=Image.open('tictactoe_b.eps')
img.save('tictactoe_b.png')

img=Image.open('tictactoe_o.eps')
img.save('tictactoe_o.png')

img=Image.open('tictactoe_x.eps')
img.save('tictactoe_x.png')

window.mainloop()
