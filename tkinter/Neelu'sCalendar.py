import tkinter as tk
from datetime import *
from math import *
from tkinter.font import Font

window = tk.Tk()

window.title("Neelu's Calendar")
window.geometry('500x500+50+50')
window.resizable(True, False)

timeNow = datetime.now().second

if timeNow%2 == 0:
    window.configure(bg='lightblue')
else:
    window.configure(bg='lightgreen') 

window['padx'] = 20
window['pady'] = 20

displayText = f"Welcome to Neelu's Calendar!\n {datetime.now()}"

label = tk.Label(window, text=displayText, font=Font(family="Helvetica", size=16, weight="bold"))
label.pack()

window.mainloop()
