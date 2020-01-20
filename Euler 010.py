import math

def is_prime(n):
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

sum = 0
for n in range(2, 2000000):
	if is_prime(n):
		sum += n

print(sum)