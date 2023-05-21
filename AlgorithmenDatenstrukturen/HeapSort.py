from random import Random


def max_heapify():
    pass


A = [i for i in range(13)]
Random().shuffle(A)

p = len(A) - 1

i = p

# p gerade und der Bruder größer)
if p % 2 == 0 and A[p] < A[p - 1]:
    i = p - 1

j = (p+1)//2
