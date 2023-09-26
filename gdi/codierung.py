import math

def hammingabstand(word1, word2):
    out = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            out += 1
    return out

def Hammingabstand_code(code):
    out = 999999999999999999999
    n = len(code)
    for i in range(n):
        for j in range(i + 1, n):
            ha = hammingabstand(code[i], code[j])
            if out > ha:
                out = ha
    return out


def informationsgehalt(wahrsch):
    r = -math.log(wahrsch/100,2)
    print(r)
    return r
