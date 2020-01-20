import math

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

size = 20

print(nCr(size * 2, size))