import tkinter as tk

window = tk.Tk()

#Code

window.title('Hello')
window.geometry("250x70")
window["bg"] = "green"
box1 = tk.Label(window, text="Hello tkinter!", bg="blue", fg="red",font=("Arial", 25))
box1.pack()

window.mainloop()

