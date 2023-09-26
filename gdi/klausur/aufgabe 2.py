import numpy

def a():
    a = numpy.int8(100)
    b = numpy.int8(170)
    print(a,b)
    print("""170 liegt nicht im Wertebereich. Deshalb wird das MSB als Vorzeichen betrachtet""")


def b():
    print("""
    GANZE ZAHL
    Exact Fließkommazahl: 1
    
    Nicht Exact Fließkommazahl: 99999999999999999999 da die mantisse nicht soviele 9nen darstellen kann
    
    Exact: 0.5
    nicht exact: 0.2 da 0.2 in binär periodisch ist
    
    
    """)
if __name__ == '__main__':
    a()
    b()