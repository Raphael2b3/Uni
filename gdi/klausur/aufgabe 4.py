from gdi import codierung as cod


def a():
    print("hamming abstand")
    r = cod.hammingabstand("0000", "0011")
    print(r)


def b():
    print("hamming abstand vom code ist der kleinste")
    code = ["0000", "0011", "0110", "1100", "1001"]
    r = cod.Hammingabstand_code(code)
    print(r)


def c():
    print("hamming abstand vom code ist der kleinste")


def e():
    print("Paritäts bit sorgt dafür das eine gerade anzahl an 1 im word enthalten ist ")




if __name__ == '__main__':
    a()
    b()