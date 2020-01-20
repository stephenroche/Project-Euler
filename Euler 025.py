from math import log10

n = 1
a = 1
b = 0

while log10(a) < 999:
	print(n, a)
	a, b = a + b, a
	n += 1

print(n)