from math import sqrt

solutions = [0] * 1001

for c in range(1, 500):
	for a in range(1, c):
		b = sqrt((c + a) * (c - a))
		if b.is_integer() and a + b + c <= 1000:
			print(a, int(b), c)
			solutions[a + int(b) + c] += 1

perimeter = max(range(1001), key=lambda i: solutions[i])
print(perimeter, solutions[perimeter] // 2)