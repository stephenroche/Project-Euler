from math import sqrt

def triangular(n):
	return int(n * (n + 1) / 2)

def num_divisors(n): # Not exact for square numbers
	num = 0
	for i in range(1, int(sqrt(n)) + 1):
		if n % i == 0:
			num += 1
	return num * 2

i = 1
while(True):
	n = triangular(i)
	if num_divisors(n) > 500:
		print(n)
		break
	i += 1