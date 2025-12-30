import tkinter as tk
from tkinter import ttk

def convert():
    print(input.get())

# window
window = tk.Tk()
window.title("Converter")
window.geometry('400x200')

#title
title_label = ttk.Label(master=window, text="Pounds to Kilograms", font="Minion 25 bold")
title_label.pack()

#input frame
input_frame = ttk.Frame(master=window)
inputInt = tk.IntVar()
input = ttk.Entry(master=input_frame, textvariable=inputInt)
button = ttk.Button(master=input_frame, text='convert', command=convert) 
input.pack(side='left', padx=5)
button.pack(side='left')
input_frame.pack(pady=20)

#output
output_label = ttk.Label(master=window, text = 'Output', font="Minion 25")
output_label.pack()

#call/run
window.mainloop()