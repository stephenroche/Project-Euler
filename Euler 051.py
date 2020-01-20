from math import sqrt

def is_prime(n):
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

for a in range(10):
	for b in range(10):
		for z in [1, 3, 7, 9]:
			primes = 0
			for x in range(10):
				if is_prime(a * 10000 + b * 100 + z + x * 101010):
					primes += 1
			print(a * 10000 + b * 100 + z, primes)
			if primes >= 8:
				print('!!!!!!!!!!!!!')



print(101010 / 7)
print(is_prime(121313))