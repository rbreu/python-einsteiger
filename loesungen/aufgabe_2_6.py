from random import randint
from sys import exit, stdin

zufall = randint(1, 100)

while True:

    print("Rate die Zahl:")
    eingabe = int(stdin.readline())

    if eingabe == zufall:
        print("Das ist richtig!")
        exit()

    if eingabe > zufall:
        print("Deine Zahl ist zu groß.")

    if eingabe < zufall:
        print("Deine Zahl ist zu klein.")
