from random import randint
from sys import exit, stdin

zufall = randint(1, 100)
versuche = 0

while True:

    print("Rate die Zahl:")
    eingabe = int(stdin.readline())
    versuche = versuche + 1

    if eingabe == zufall:
        print("Das ist richtig! Anzahl Versuche:", versuche)
        exit()

    if eingabe > zufall:
        print("Deine Zahl ist zu groß.")

    if eingabe < zufall:
        print("Deine Zahl ist zu klein.")
