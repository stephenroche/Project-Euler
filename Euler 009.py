for a in range(1, 1000):
	for b in range(1, a):
		c = 1000 - a - b
		if a**2 + b**2 == c**2:
			print('%d * %d * %d = %d' % (a, b, c, a * b * c))