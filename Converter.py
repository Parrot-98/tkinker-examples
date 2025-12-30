import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Converter")
window.geometry('500x200')

#title
title_label = ttk.Label(master=window, text="Pounds to Kilograms", font="Minion 25 bold")
title_label.pack()

#input frame
input_frame = ttk.Frame(master=window)
input = ttk.Entry(master=input_frame)
button = ttk.Button(master=input_frame, text='convert')
input.pack()
button.pack()
input_frame.pack()

#call/run
window.mainloop()