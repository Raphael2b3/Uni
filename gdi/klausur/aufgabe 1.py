import gdi.konvertierung as kon

BASIS = 16
def a():
    matrikelnummer = 82832
    result = kon.schriftlich_dez2n(matrikelnummer, BASIS)
    print(result)
    return result

def b(hex):
    r = kon.hex2bin(hex)

    print("""
    Ziffern von Hex-Zahlen einzeln in binär umwandeln. 1 Ziffer = 4 bit
    
    """)
    print(r)

def c():
    print("""
    1. Grund Die gegebne Binärzahl ist ungerade (LSB=1) und 14 ist eine Grade Zahl
    2. Grund Die binärzahl ist deutlich größer als 14, 1*2^4
    """)


def d(basis=13, stellen=3): # höchste zahl in basis
    out = 0
    for i in range(stellen):
        out += (basis-1)*13**(i)
        print((basis-1),"*",basis,"^",(i), "+")
    print(out)
    return out

def e():
    zahlen = [[[8,0],9],[[4,2],21],[[4,2],18]]

    for zahl in zahlen:
        kon.schriftlich_n2dez(zahl[0],zahl[1])

    print("""
    
    MSB Betrachten
     
    """)



if __name__ == '__main__':
    print("1 2 3 4 5 6 7 8 9  A  B  C  D  E  F")
    print("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15")
    a1 = a()
    b(a1)
    c()
    d()
    e()