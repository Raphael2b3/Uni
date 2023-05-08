import math
import random


def merge_sort(arr):
    i = len(arr) // 2
    if not i: return arr
    l = merge_sort(arr[:i])
    r = merge_sort(arr[i:])
    out = []
    while len(l) > 0 and len(r) > 0:
        out.append((r if l[0] >= r[0] else l).pop(0))
    return out + l + r


def fill_array(anzahl, von=0, bis=100): #Funktion zum Erstellen eiens Arrays der Länge "anzahl" mit zufälligen Zahlen der Größe von-bis
    unsortierte_zahlen = []
    for i in range(anzahl):
        unsortierte_zahlen.append(random.randint(von, bis))
    return unsortierte_zahlen


if __name__ == '__main__':
    print("DEVIDE AND CONQUER -- TEILE UND HERRSCHE")
    message = """Kurz D&C
    Größere Probleme werden in kleinere zerleht, die dann seperat gelöst werden.
    Die Teilergebnisse werden wieder zusammen gesetzt"""
    print(message)
    arr = fill_array(20)
    print("Unsorted:")
    print(arr)
    arr = merge_sort(arr)
    print(arr)

