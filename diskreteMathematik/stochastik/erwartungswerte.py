def F(x, verteilung):
    out = 0
    for i in verteilung:
        if i > x: break
        out += verteilung[i] * i
    print(f"F({x})=",out)
    return out

def erwartungswert_mü(verteilung,gx=None):
    # mü , u
    out = 0
    for i in verteilung:
        out += i * (1/len(verteilung) if not gx else gx(i))
    return out

def varianz_sigmaQuadrat(verteilung):  # mü , u

    erwartWert = erwartungswert_mü(verteilung)
    print("Erwartungswert mü = ", erwartWert)
    out = erwartungswert_mü(verteilung, lambda x: (x - erwartWert) ** 2)
    print("Varianz sigma^2=", out)

    return out

def standartabweichung_sigma(verteilung):
    t = varianz_sigmaQuadrat(verteilung)

    print("Standartabweichung sigma=", t ** 0.5)

    return t ** 0.5


if __name__ == '__main__':
    a = 6/343
    def fff(x):
        return a*(-(x**3)/3 - 3*x**2 + 10*x + 275)
    verteilung = {}
    def px(x):
        delta = 0 if x < -5 else 1 if x < 3 else 0
        return fff(x) - fff(x-delta)
    for i in range(-5, 3):
        verteilung[i] = a*(-(i**3)/3 - 3*i**2 + 10*i + 275)
    F(8.5, verteilung)

    print(erwartungswert_mü(verteilung))

    standartabweichung_sigma([7.74 ,9.16, 4.95, 6.61 ,6.28 ,8.59 ,5.26 ,6.47])