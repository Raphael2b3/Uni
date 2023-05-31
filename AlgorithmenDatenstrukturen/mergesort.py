def merge(a, b):
    out = []
    while len(a) and len(b):
        out.append(a.pop(0) if a[0] < b[0] else b.pop(0))
    out += a + b
    return out


def mergesort(l):
    div = len(l) // 2
    if div == 0: return l

    a = l[:div]  # split
    b = l[div:]  # divide

    a = mergesort(a)  # sort a
    b = mergesort(b)  # sort b

    return merge(a, b)  # merge a,b efficient

