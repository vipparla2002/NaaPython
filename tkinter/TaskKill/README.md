 # 🛑 Task Kill GUI (Windows)

A simple **Tkinter-based GUI application** that allows you to terminate running Windows processes using `taskkill`.

This tool provides a graphical interface to kill specific processes by name or quickly terminate Google Chrome if no process name is provided.

---

## 📌 Features

* Kill a specific running process by entering its name
* Force kill (`/F`) enabled
* Terminates child processes (`/T`)
* Simple and lightweight GUI
* Refresh button to update UI state

---

## 🖥️ How It Works

* The program runs the Windows `tasklist` command.
* It searches for the entered process name.
* If found, it executes:

  ```
  taskkill /F /IM process_name /T
  ```
* If no process name is entered, it defaults to killing:

  ```
  chrome.exe
  ```

---

## ⚙️ Requirements

* Windows OS
* Python 3.x
* Tkinter (comes pre-installed with standard Python on Windows)

---

## 🚀 How to Run

1. Save the script as:

   ```
   task_kill_gui.py
   ```
2. Open Command Prompt in the file directory.
3. Run:

   ```
   python task_kill_gui.py
   ```

---

## 📝 Usage

1. Enter the **process name** (example: `notepad.exe`, `chrome.exe`)
2. Click **"Task Kill"**
3. The result label will show how many processes were terminated
4. Click **"Refresh"** to update the UI

---

## ⚠️ Warning

* This program uses **force termination (`/F`)**, which immediately stops processes.
* Unsaved work in terminated applications will be lost.
* Use carefully.

---

## 📂 Project Structure

```
task_kill_gui.py
README.md
```

---

## 🔒 Notes

* Administrator privileges may be required to terminate certain system processes.
* The application only works on **Windows**, as it relies on `tasklist` and `taskkill`.

---

## 📜 License

This project is open-source and free to use for learning purposes.

---
