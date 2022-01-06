import tkinter as tk
from tkinter.constants import BOTTOM
import random
# Grabbelton

# Een GUI opend met een knop er in waarop grabbelen staat
# Een label met het aantal items in de grabbelton
# Als je op de knop drukt moet je het bericht te zien krijgen: “Gefeliciteerd, je hebt een {item} gegrabbeld!”
# Op de plek van {item} in de tekst moet een woord komen die je random uit een lijst met minimaal 10 verschillende woorden haalt
# Daarna moet het aantal items worden aangepast en mag dat woord niet meer terug komen.
# gum, sleutelhanger, stuiterbal, potloden, spelletje, puzzel, snoep, zaklamp, stickers, stempels

grabbelton = ["gum","sleutelhanger","stuiterbal","potlood","spelletje","puzzel","snoepje","zaklamp","sticker","stempel"]

def grabbelen():
    item = random.choice(grabbelton)
    Text.set("Gefeliciteerd, je hebt een "+ item +" gegrabbeld")
    label2.configure(textvariable=Text)
    grabbelton.remove(item)
    
    if len(grabbelton) > 0:
        Text2.set("Er zitten nog "+ str(len(grabbelton)) +" items in de grabbelton")
        label3.configure(textvariable=Text2)
    elif len(grabbelton) == 0:
        Text.set("De grabbelton is leeg")
        label2.configure(textvariable=Text)
        Text2.set("")
        label3.configure(textvariable=Text2)

window = tk.Tk()
window.geometry("400x100")
window.title("Grabbelton")
window["bg"] = "white"
window.eval('tk::PlaceWindow . center') # optioneel (puur om het scherm in het midden te krijgen)
Text = tk.StringVar(value="")
Text2 = tk.StringVar(value="")
label = tk.Label(text="Druk op ENTER om een item uit de grabbelton te pakken", bg="white")
label.pack()
label2 = tk.Label(textvariable=Text, bg="white")
label2.pack()
label3 = tk.Label(textvariable=Text2, bg="white")
label3.pack()
button = tk.Button(text="Grabbelen!",bd=0, command=grabbelen)
button.pack(side=BOTTOM)
grabbelton = ["gum","sleutelhanger","stuiterbal","potlood","spelletje","puzzel","snoep","zaklamp","stickers","stempels"]


window.mainloop()




