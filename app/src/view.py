import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title('Catering app - BD2')
        self.geometry('600x400')

        self.label = tk.Label(self, text = 'Hello catering')
        self.label.grid(column = 0, row = 0)
