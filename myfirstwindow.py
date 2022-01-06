import tkinter

window = tkinter.Tk()

# Maak een programma die een venster opent met de titel “My First Window” 
# met een witte achtergrond en een grote heeft van 50 bij 50 en vervolgens iedere 2 seconden van kleur en grote (50 hoger en 50 breeder) veranderd.
# "red", "green", "blue", "cyan", "yellow", "magenta"

#Code
colors = ["", "green", "blue", "cyan", "yellow", "magenta"]
hoogte = 50
breedte = 50
i = 6

def explosionWindow(i, hoogte, breedte):
    while i > 0:
        window.update()
        window.geometry(f"{hoogte}x{breedte}")
        window["bg"] = colors[0]
        colors.remove(colors[0])
        window.after(2000)
        print(i)
        
        i-=1
        hoogte+=50
        breedte+=50
    if i == 0:
        print("BOOM!")
        window.destroy()

window.title("My First Window")
window.geometry("50x50")
window["bg"] = "white"
explosionWindow(i, hoogte, breedte)

window.mainloop()