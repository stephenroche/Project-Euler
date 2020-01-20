primes = [False] * 1000000

from math import sqrt, log10

def is_prime(n):
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

primes[2] = True
for n in range(3, 1000000, 2):
	if n % 10000 == 1:
		print(n)
	primes[n] = is_prime(n)

def shift(n):
	return n // 10 + (n % 10) * 10 ** int(log10(n))

circular_primes = 0
for n in range(2, 1000000):
	if primes[n]:
		curr = shift(n)
		while primes[curr]:
			curr = shift(curr)
			if curr == n:
				print(n)
				circular_primes += 1
				break
print(circular_primes)