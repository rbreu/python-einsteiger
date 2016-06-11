
# Einstieg in die Programmierung mit Python

*Rebecca Breu, Thomas Koch*


## Warum Python?

* Einfache, klare Syntax, daher leicht zu lernen
* Komplette Programmiersprache mit vielen Bibliotheken, kann in vielen Feldern eingesetzt werden, z.B. Webentwicklung, wissenschafltiches Rechnen, Serveradministration, ...
* Auf dem Raspberry Pi sehr verbreitet
* Implementation für Mikroprozessoren existiert
* ...


In dieser Einführung benutzen wir **Python 3**. Immer noch sehr verbreitet ist Python 2, allerdings ist es nicht kompatibel zu Python 3. 

Benötigt werden: 
* Installation von [Python 3](https://www.python.org/downloads/). Auf den meisten Linux-Systemen (z.B. Raspbian) sind sowohl Python 2 als auch Python 3 standardmäßig installiert.
* Ein Editor, z.B. Gedit, Atom, Sublime, ...

## Teil 1: Erste Schritte in der Konsole

Man kann Python direkt in der interaktiven Python-Konsole verwenden. 

* *Vorteil:* Man kann schnell und einfach Dinge ausprobieren
* *Nachteil:* Code wird nicht dauerhaft gespeichert, kann nicht wiederverwendet werden

**Aufgabe 1-1:** Starte ein Terminal-Fenster. Starte Python mit dem Befehl `python3`:

```
camptut@infcip10:~$ python3
Python 3.4.3 (default, Oct 14 2015, 20:28:29) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Die drei Pfeile `>>>` zeigen an, dass Python auf Eingabe wartet. Mit `exit()` oder `Steuerung + d` kannst du Python wieder beenden.


**Aufgabe 1-2:** Python als Taschenrechner

Probiere die vier Grundrechenarten aus: + (Addidion), - (Subtraktion), * (Multipikation) und / (Division)

Zum Beispiel:


```python
13 + 4 - 3
```




    14




```python
17 / 2
```




    8.5



Dezimalzahlen werden in Python mit einem Dezimalpunkt angegeben, nicht mit einem Dezimalkomma: `1.25`

Du kannst auch Klammern verwenden:


```python
(4 + 10) * 2.5
```




    35.0



Wieviele Sekunden hat eine Stunde? Wieviele Sekunden hat ein Tag?

** Aufgabe 1-3:** Variablen

Variablen sind Namen für Dinge, die man wiederverwenden will. Man benzutzt ein Gleichheitszeichen, um Variablen zuzuweisen, zum Beispiel:


```python
laenge = 12
breite = 4
laenge * breite
```




    48




```python
laenge = 12
breite = 4
flaeche = laenge * breite
print(flaeche)
```

    48


``print`` (deutsch: drucken) ist eine Funktion, um etwas auf dem Bildschirm auszugeben. Wir werden sie später noch öfter brauchen.

**Aufgabe 1-4:** Strings

Strings (deutsch: Zeichenketten) sind Texte, die du beim Programmieren verwenden kannst. Z.B.:


```python
name = "Rebecca"
print(name)
```

    Rebecca



```python
name = 'Thomas'
print(name)
```

    Thomas


Man kann einfache (') oder doppelte (") Anführunszeichen benutzen, um einen String zu erzeugen. Wichtig ist, dass am Anfang und Ende eines Strings die gleiche Art von Anführunszeichen benutzt.


```python
vorname = "Rebecca"
nachname = "Breu"
vorname + nachname
```




    'RebeccaBreu'



Wie bekommnt man ein Leerzeichen zwischen Vor- und Nachname?

**Aufgabe 1-5:** Fehler

Beim Programmieren macht man immer wieder Fehler. Das ist überhaupt nicht schlimm, und Python versucht immer, zu erklären, was falsch ist. 

Verstehst du, was bei den untenstehenden Codestücken falsch ist?


```python
10 / 0
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-26-3e699e72a4ab> in <module>()
    ----> 1 10 / 0
    

    ZeroDivisionError: division by zero



```python
vorname = "Rebecca"
nachname = "Breu"
vorname * nachname
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-28-0812ef918b26> in <module>()
          1 vorname = "Rebecca"
          2 nachname = "Breu"
    ----> 3 vorname * nachname
    

    TypeError: can't multiply sequence by non-int of type 'str'



```python
vorname = "Rebecca"
print(voname)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-31-a8833e6e0711> in <module>()
          1 vorname = "Rebecca"
    ----> 2 print(voname)
    

    NameError: name 'voname' is not defined


## Teil 2: Programme schreiben

Nun wollen wir Programme schreiben, die wir immer wieder aufrufen können, ohne sie jedes mal neu tippen zu müssen. Dazu schreiben wir unseren Python-Code in eine Datei.

[Die Lösungen zu den folgenden Aufgaben findest du online.](https://github.com/rbreu/python-einsteiger/tree/master/loesungen)

**Aufgabe 2-1** Das erste Programm

Öffne den Editor **gedit**. Schreibe dein erstes Python-Programm:


```python
# Mein erstes Programm
# Aufgabe 2-1

summe = 7 + 12
print(summe)
```

Zeilen, die mit einer Raute (#) beginnen, werden von Python ignoriert. Du kannst hier Kommentare schreiben, die dir helfen, das Programm zu verstehen. Du kannst an beliebigen Stellen Leerzeilen lassen, um den Code übersichtlicher zu machen.

Speichere die Datei unter dem Namen `programm1.py` in deinem Home-Verzeichnis. Python-Programme sollten immer die Datei-Endung `.py` haben. Dann öffne ein Linux-Terminal (ohne die interaktive Python-Schell) und führe dein Programm aus mit `python3 programm1.py`:

```bash
camptut@infcip10:~$ python3 programm1.py
19
```

Alle Ausgaben, die du in der Kosole sehen möchtest, musst du mit ``print`` ausgeben.

Ändere das Programm so ab, dass es deinen Namen ausgibt.

**Aufgabe 2-2** Der Addierer

Hast du eine Idee, was das folgende Programm macht? Probiere es aus!


```python
from sys import stdin

print("Gib eine Zahl ein:")
eingabe = int(stdin.readline())

summe = eingabe + 7

print("Die Summe ist:", summe)
```

In der ersten Zeile importieren wir `stdin` aus der Python-Bibliothek `sys`. Die meisten Funktionen von Python sind in Bibliotheken strukturiert und wir müssen sie importieren, um sie nutzen zu können. Die dritte Code-Zeile verwendet das importierte `stdin`, um eine Benutzereingabe zu lesen. (stdin steht für standard input, deutsch Standard-Eingabe.)

Schreibe das Programm so um, dass der Nutzer zwei Zahlen eingeben kann, deren Summe dann ausgegeben wird.

**Aufgabe 2-3** Schleifen

Mit einer for-Schleife können wir Python ganz einfach mitteilen, dass ein bestimmter Programmteil wiederholt werden soll. Das folgende Programm gibt alle Zahlen von 1 bis 10 aus:


```python
for i in range(1, 11):
    print("Die aktuelle Zahl lautet:")
    print(i)
print("Nun ist die Schleife zuende.")
```

`range(1, 11)` liefert die Zahlen von 1 bis 10. Die Anweisung `for` besagt, dass der nachfolgende Codeblock so oft wiederholt werden soll, wie die range-Funktion Zahlen liefert. Die aktuelle Zahl jedes Schleifendurchlaufs ist in der Variable `i` verfügbar. In Schleifen wird häufig der Variablenname `i` benutzt, du kannst aber auch einen anderen Namen wählen.

Der Codeblock, der eingerückt ist (nimm am besten immer 4 Leerzeichen zur Einrückung), gehört zur Wiederholung der Codeschleife. Die letzte Zeile ist nicht mehr eingerückt und wird erst ausgeführt, nachdem alle 10 Schleifendurchläufe beendet sind.

Ändere das Programm so ab, dass die Zahlen von 1 bis 20 ausgegeben werden.

Ändere das Programm so ab, dass das Ein-Mal-Drei ausgegeben wird. (1, 3, 6, ..., 30).

Ändere das Programm so ab, dass der Nutzer eine Zahl eingibt und dann das Ein-Mal-... dieser Zahl ausgegeben wird. Gibt der Nutzer eine 4 ein, wird das Ein-Mal-Vier ausgegeben usw.

**Aufgabe 2-4** Aufsummieren

Was macht folgender Code? 


```python
summe = 5
summe = summe + 4
print(summe)
```

    9


Die zweite Zeile sieht auf den ersten Blick merkwürdig aus. Hier nimmt Python zunächst die rechte Seite vom Gleichheitszeichen, also "summe + 4", rechnet das Ergebnis aus, also 9, und weist das Ergebnis wieder der Variablen `summe` zu. In anderen Worten: In der zweiten Zeile wird die Variable `summe` im 4 erhöht.

Benutze nun eine solche Anweisung in einer for-Schleife, um alle Zahlen von 1 bis 100 aufzuaddieren. Als Ergebnis solltest du 5050 herausbekommen.

**Aufgabe 2-5** If-Bedingungen

Mit if-Bedingungen kann man Code-Teile nur unter bestimmten Bedingungen ausführen lassen. Versuche, das folgende Programm zu verstehen:


```python
from sys import stdin

print("Gib eine Zahl ein:")
eingabe = int(stdin.readline())

if eingabe > 10:
    print("Deine Zahl ist größer als 10")

if eingabe == 10:
    print("Deine Zahl ist gleich 10")

if eingabe < 10:
    print("Deine Zahl ist kleiner als 10")
```

Das, was nach dem `if` steht, ist die Bedingung, die erfüllt werden muss, damit der nachfolgende Codeblock ausgeführt wird. Wie schon bei den for-Schleifen wird durch Einrückung (vier Leerzeichen!) angegeben, was zum Codeblock dazugehört.

Beachte, dass die Prüfung auf Gleichheit mit einem doppeltem Gleichzeichen erfolgt: `==`

Probiere das obige Programm aus.

**Aufgabe 2-6** Zahlenraten

Programmiere das Spiel Zahlenraten. Das Programm wählt eine zufällige Zahl zwischen 1 und 100, die der Spieler raten muss. Das Programm erwartet eine Eingabe vom Spieler und sagt, ob die eingegebe Zahl größer oder kleiner als die zu ratende Zahl ist. Ist die Zahl gleich, beendet das Programm, ansonsten darf der Spieler es noch einmal probieren.

Erweitere dazu folgendes Programm:


```python
from random import randint
from sys import exit, stdin

# Eine Zufallszahl zwischen 1 und 100 generieren:
zufall = randint(1, 100)

# Eine Schleife, die unendlich lange läuft:
while True:

    ...

    if ... == ...:
        print("Das ist richtig!")
        # Das Programm beenden:
        exit()

    ...
```

Wenn du das geschafft hast, kannst du auch mitzählen, wieviele Versuche der Spieler gebraucht hat und das am Ende ausgeben.

## Weiterführende Links

* [Python 3-Tutorial](https://py-tutorial-de.readthedocs.io/de/python-3.3/) - Deutsch
* [Python 3-Dokumentation](https://docs.python.org/3/library/index.html) - Englisch
* [Code Combat](https://codecombat.com/) - mehrsprachig - Programmierlernspiel
* [Python lernen auf dem Raspberry Pi](https://www.youtube.com/channel/UCRAvo5cQWyfog8nRzlf_jWg) - Englisch - Videoreihe
* [Python Challenge](http://www.pythonchallenge.com/) Eine Serie von Programmieraufgaben in Form von Rätseln - Englisch. Eher für Leute, die schon die ersten Python-Erfahrungen gesammelt haben.
* [PEP 8](https://www.python.org/dev/peps/pep-0008/) Styleguide für Python-Programme
* [... weitere Linksammlung](http://wiki.pythonde.pysv.org/Tutorial)

## Bücher

* Raspberry Pi programmieren mit Python, Michael Weigend
* Python kinderleicht!, Jason Briggs
* Python für Kids, Gregor Lingl
* Python 3: Das umfassende Handbuch, Johannes Ernesti und Peter Kaiser
* Einstieg in Python, Thomas Theis

## Sonstiges

* [IPython](https://ipython.org/): Interaktive Python-Umgebung, die wesentlich komfortabler ist als die normale Python-Umgebung.
* [MicroPython](https://micropython.org/): Python-Implementierung für Microprozessoren.




```python

```
