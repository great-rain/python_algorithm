def factorial(n:int):
    if n == 0:
        return 1
    return factorial(n-1)*n

print(factorial(int(input())))