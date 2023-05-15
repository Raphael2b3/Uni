from random import Random

def MaxHeapify():
    pass




A = [i for i in range(13)]
Random().shuffle(A)

l = len(A)-1

i = l

if i%2 ==1 or A[l]>A[l-1]:
    i = l
else:
    i = l-1






