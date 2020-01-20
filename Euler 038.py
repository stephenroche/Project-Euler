for n in range(9182, 10000):
	if sorted(list(str(n)) + list(str(2 * n))) == [str(d) for d in range(1, 10)]:
		print(n, 2 * n)