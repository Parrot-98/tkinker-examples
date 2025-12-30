import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Converter")
window.geometry('500x200')

#title
title_label = ttk.Label(master=window, text="Pounds to Kilograms", font="Minion 25 bold")
title_label.pack()

#call/run
window.mainloop()