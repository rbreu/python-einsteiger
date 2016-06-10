from sys import stdin

print("Gib eine Zahl ein:")
eingabe = int(stdin.readline())

print("Das 1 mal", eingabe)

for i in range(1, 11):
    print(i * eingabe)
