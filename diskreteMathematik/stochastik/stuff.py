p1m = 912
p2m = 1383
p3m = 996
p4m = 1490

p1 = 0.04
p2 = 0.07
p3 = 0.07
p4 = 0.022

a = p1*p1m + p2*p2m + p3*p3m + p4*p4m

final = p1m + p2m + p3m + p4m
fail = a/final

v1 = p1m/final
v2 = p2m/final
v3 = p3m/final
v4 = p4m/final

if __name__ == '__main__':
    print(a)
    print(fail*v1)
    print(fail*v2)
    print(fail*v3)
    print(fail*v4)
