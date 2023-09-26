import numpy

def a():

    a = numpy.int8(16)
    print(1, a>>1)
    print(2, a<<1)
    print(3, a&1)
    print(4, a^1)


def b():
    print("Masken vergleich mit verundung 0b1000")
if __name__ == '__main__':
    a()
    b()