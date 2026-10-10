def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

n = int(input("Calculate the following fibonacci number: "))
print(fib(n))