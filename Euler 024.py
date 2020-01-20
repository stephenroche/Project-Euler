def fac(n):
	if n == 1:
		return 1
	else:
		return n * fac(n - 1)

n = 1000000 - 1
multiples = []
for i in range(9, 0, -1):
	multiples.append(n // fac(i))
	# print(multiples[-1])
	n -= multiples[-1] * fac(i)

multiples.append(0)
print(multiples)

one_to_ten = [i for i in range(10)]
print(one_to_ten)

for i in multiples:
	print(one_to_ten.pop(i), end='')