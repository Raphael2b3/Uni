def a():
    def x(a, b, c):
        return int(a and b)

    def y(a, b, c):
        return int(b or not c)

    def z(a, b, c):
        return int(x(a, b, c) != y(a, b, c))
    return x, y, z


def b(x, y, z):
    print("a b c | x y z")
    for a in range(2):
        for b in range(2):
            for c in range(2):
                print(a, b, c,"|", x(a, b, c), y(a, b, c), z(a, b, c))

def c():
    #https://kmio.de/logikrechner.html
    print("kv diagramm")

if __name__ == '__main__':
    x, y, z = a()
    b(x, y, z)
    c()
