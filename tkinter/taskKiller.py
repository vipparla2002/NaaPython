import tkinter as tk
import os
import time

def taskKill():
    os.system("taskkill /F /IM chrome.exe /T")
    os.system("taskkill /F /IM chromedriver.exe /T")

    result.config(text="Task Kill Executed", bg="light blue", fg="black", font=("Arial", 16))
    # if(os.system("tasklist | findstr chrome") != 0):
    #     result.config(text="", bg="light green", fg="black", font=("Arial", 16))

def refresh_function():

    window.update()
    window.update_idletasks()
    result.config(text="refreshed", bg="light blue", fg="black", font=("Arial", 16))

window = tk.Tk()

window.title("Task Kill")

window.geometry('350x350')
window.resizable(True, True)

#######################

button = tk.Button(window, text="Task Kill", command=taskKill,background="lemon chiffon", fg="purple", font=("Arial", 24))

refreshButton = tk.Button(window, text="Refresh", command=refresh_function,background="lemon chiffon", fg="purple", font=("Arial", 24))


result = tk.Label(window, height=10, width=50)

refreshButton.pack()
button.pack()
result.pack() 

window.mainloop()