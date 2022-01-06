import random,time
# Grabbelton

# Een GUI opend met een knop er in waarop grabbelen staat
# Een label met het aantal items in de grabbelton
# Als je op de knop drukt moet je het bericht te zien krijgen: “Gefeliciteerd, je hebt een {item} gegrabbeld!”
# Op de plek van {item} in de tekst moet een woord komen die je random uit een lijst met minimaal 10 verschillende woorden haalt
# Daarna moet het aantal items worden aangepast en mag dat woord niet meer terug komen.
# gum, sleutelhanger, stuiterbal, potloden, spelletje, puzzel, snoep, zaklamp, stickers, stempels

grabbelton = ["gum","sleutelhanger","stuiterbal","potlood","spelletje","puzzel","snoep","zaklamp","stickers","stempels"]


def grabbelen(grabbelton):
    item = random.choice(grabbelton)
    print("Gefeliciteerd, je hebt een", item ,"gegrabbeld")
    grabbelton.remove(item)
    
    if len(grabbelton) > 0:
        print("Er zitten nog", len(grabbelton), "items in de grabbelton")

while len(grabbelton) > 0:
    time.sleep(0.5)
    input("Druk op ENTER om een item uit de grabbelton te pakken ")
    print()
    grabbelen(grabbelton)
        
    if len(grabbelton) == 0:
        print("De grabbelton is leeg")





