import tkinter as tk


class GuiDemo:
    """
    Gui Demo from Edube.org

    Demonstrate multiple types of widgets:
    -- label, frame, button, checkbutton, radiobutton
    """

    def __init__(self):
        def digits_only(*args):
            global last_string
            string = self.text_2.get()
            print(string)
            if string == '' or string.isdigit():  # Field's content is valid.
                last_string = string
            else:
                self.text_2.set(last_string)

        self.window = tk.Tk()

        self.label = tk.Label(self.window, text="Little label:")
        self.label.pack()

        self.frame = tk.Frame(self.window, height=50, width=100, bg="#000099")
        self.frame.pack()

        self.button = tk.Button(self.window, text="Button")
        self.button.pack()

        self.switch = tk.IntVar()
        self.switch.set(1)

        self.checkbutton = tk.Checkbutton(self.window, text="Check Button", variable=self.switch)
        self.checkbutton.pack()

        self.text_2 = tk.StringVar()
        self.entry = tk.Entry(self.window, textvariable=self.text_2, width=30)
        self.last_string = '1234'
        self.text_2.set(self.last_string)
        print(self.last_string)
        self.text_2.trace('w', digits_only)
        self.entry.focus_set()
        self.entry.pack()

        self.radiobutton_1 = tk.Radiobutton(self.window, text="Steak", variable=self.switch, value=0)
        self.radiobutton_1.pack()
        self.radiobutton_2 = tk.Radiobutton(self.window, text="Salad", variable=self.switch, value=1)
        self.radiobutton_2.pack()

        self.text = tk.StringVar()
        self.message = tk.Message(self.window, textvariable=self.text, width=400)
        self.text.set("You did it again... ")
        self.message.pack()

        self.window.mainloop()

x = GuiDemo()
