def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


for i in range(1,10000):
    print(fib(i + 1)/fib(i))
