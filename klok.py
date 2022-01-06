import tkinter
root = tkinter.Tk()



currentTime = tkinter.StringVar(value="Welkom")
label = tkinter.Label(root)
label.configure(textvariable=currentTime)
label.pack()


def updateLabel():
    firstMessage = currentTime.get()
    currentTime.set(firstMessage + "Gebruiker")


updateLabel()
root.mainloop()
