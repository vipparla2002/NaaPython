import subprocess
import tkinter as tk
import time

def taskKill():

    textInputCleaned  = textInput.get().strip().lower()

    taskList = subprocess.run("tasklist", capture_output=True, text=True, shell=True)

    killed_count = 0
    killed_processes = []

    for line in taskList.stdout.splitlines():

        if  not textInputCleaned:
            subprocess.run(f"taskkill /F /IM chrome.exe /T", shell=True) 

        elif textInputCleaned in line.lower():
            process_name = line.split()[0]  # First column = process name
            try:
                subprocess.run(f"taskkill /F /IM {process_name} /T", shell=True)
                killed_count += 1
                killed_processes.append(process_name)
            except:
                pass
        
    
    result.config(text=f"Task Kill Executed. Killed {killed_count}", bg="light blue", fg="black", font=("Arial", 16))
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

#  Input Label
input_label = tk.Label(window, text="Enter Process Name:", font=("Arial", 14))
input_label.pack(pady=5)

#  Text Box
textInput = tk.Entry(window, font=("Arial", 14), width=25)
textInput.pack(pady=5)
#######################

button = tk.Button(window, text="Task Kill", command=taskKill,background="lemon chiffon", fg="purple", font=("Arial", 24))

refreshButton = tk.Button(window, text="Refresh", command=refresh_function,background="lemon chiffon", fg="purple", font=("Arial", 24))


result = tk.Label(window, height=10, width=50)

refreshButton.pack()
button.pack()
result.pack() 

window.mainloop()