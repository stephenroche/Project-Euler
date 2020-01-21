for n in range(9182, 9500):
	if sorted(list(str(n)) + list(str(2 * n))) == list('123456789'):
		print(n, 2 * n)