import math

def is_prime(n):
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

primes = 0
n = 1
while primes < 10001:
	n += 1

	if is_prime(n):
		primes += 1
	
print(n)