"""
            Global AI Hub  
        Introduction to Python 
      Homework III — Ugurcan Dede
"""
from random import choice
kelime = choice(["globalaihub", "turkishhub", "python", "homework"])

user = input("Hi! What's your name?\n")
print("Welcome {}, let's get start\n\n".format(user))

tahmin = []
yanlis = []

hak = 7
while hak > 0:
    bulunan = ""

    for l in kelime:
        if l in tahmin:
            bulunan  += l
        else:
            bulunan  += "_"

    if bulunan == kelime:
        break

    print("Guess the word: ", bulunan)
    print(hak, "chances left")

    t_giris = input('Guess a letter: ')

    if t_giris in tahmin or t_giris in yanlis:
        print("Already guessed", t_giris)

    elif t_giris in kelime:
        print("Yayyy!\n")
        tahmin.append(t_giris)

    else:
        print("Nope\n")
        hak -= 1
        yanlis.append(t_giris)
        
if hak:
    print("Congratulations! You guessed {} word correctly".format(kelime))
else:
    print("You did not guess {} word correctly".format(kelime))