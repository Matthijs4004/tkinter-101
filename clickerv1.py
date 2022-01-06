# Clicker v1
import tkinter as tk
from tkinter import IntVar
from tkinter.constants import NUMERIC
# 1 knop zorgt er voor dat het nummer in de label met 1 omhoog gaat
# 1 knop zorgt er voor dat het nummer in de label met 1 omlaag gaat.
# Als het nummer 0 is moet de achtergrond grijs zijn.
# Als het nummer kleiner dan 0 is moet de achtergrond rood zijn.
# Als het nummer groter dan 0 is moet de achtergrond groen zijn.

def Up():
    global number
    number.set(number.get() + 1)
    Label.configure(textvariable=number)
    if number.get() > 0:
        window["bg"] = "green"
    elif number.get() < 0:
        window["bg"] = "red"
    else:
        window["bg"] = "grey"

def Down():
    global number
    number.set(number.get() - 1)
    Label.configure(textvariable=number)
    if number.get() < 0:
        window["bg"] = "red"
    elif number.get() > 0:
        window["bg"] = "green"
    else:
        window["bg"] = "grey"

window = tk.Tk()
window.title("Clicker v1")
window.geometry("250x200")
window["bg"] = "grey"
window.eval('tk::PlaceWindow . center') # optioneel (puur om het scherm in het midden te krijgen)
number = IntVar(value=0)
buttonUp = tk.Button(bg="white", width=20, text="Up", bd=0, command=Up)
Label = tk.Label(bg="white",width=20, textvariable=number)
buttonDown = tk.Button(bg="white",width=20, text="Down", bd=0, command=Down)
buttonUp.place(y=45,x=50)
Label.place(y=100,x=50)
buttonDown.place(y=150,x=50)



window.mainloop()