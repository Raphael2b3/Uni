from gdi import codierung as cod
def a():
    häufigkeiten = {"A": 34, "B": 27, "C": 5, "D": 16, "E": 18}
    r = cod.informationsgehalt(häufigkeiten["D"])
    print("informationsgehalt formel ", r)

def b():
    print("""kleinster Informationsgehalt(da die Relative Häufigkeit am gößten ist)""")

if __name__ == '__main__':
    a()
    b()
