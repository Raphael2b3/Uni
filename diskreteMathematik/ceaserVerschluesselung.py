start = ord("A")
ende = ord("Z") + 1
dif = ende - start

print(start, ende, dif)

def ceasar_verschluesseln(wort, schluessel):
    out = ""
    for w in wort:
        o = keyvalue(w)

        z = (o + schluessel) % dif + start
        out += chr(z)
    return out


def ceasar_entschluesseln(wort, schluessel):
    return ceasar_verschluesseln(wort, -schluessel)

def keyvalue(c):
    return ord(c) - start


start = ord("A")
ende = ord("Z") + 1
dif = ende - start

def vigenere(wort, schluessel):
    le = len(schluessel)
    out = ""
    i = 0
    for w in wort:
        k = keyvalue(w)
        lv = keyvalue(schluessel[i % le])
        out += chr((k + lv)%dif + start)
        i += 1
    return out


a = ceasar_verschluesseln("AVEYRON", 11)
print(a)
a = Vigenere("AVEYRON","FRZ")
print(a)