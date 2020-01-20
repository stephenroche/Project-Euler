n = 600851475143
factor = 2
while n != 1:
	if n % factor == 0:
		n /= factor
		print(factor)
	else:
		factor += 1

