def num_terms(n):
	terms = 1
	while n != 1:
		if n % 2 == 0:
			n /= 2
		else:
			n = 3 * n + 1
		terms += 1
	return terms

print(num_terms(1000000))

max = 0
for n in range(1, 1000000):
	terms = num_terms(n)
	if terms > max:
		max = terms
		print('terms(%d) = %d' % (n, terms))