import tkinter as tk
from time import strftime
from tkinter import font
from typing import Text

window = tk.Tk()

window.title("Klok")
window.geometry("200x50")
window["bg"] = "white"

currentTime = tk.StringVar(value=strftime("%H: %M: %S"))
klok = tk.Label(window, bg="white", font=("Calibri Light", 20, font.BOLD))
klok.configure(textvariable=currentTime)
klok.pack()

def updateLabel():
    currentTime.set(strftime("%H: %M: %S"))
    klok.configure(textvariable=currentTime)
    klok.after(80, updateLabel)

updateLabel()
window.mainloop()