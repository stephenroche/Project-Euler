from math import sqrt

def is_prime(n):
	if n < 2:
		return False
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

primes = []
for i in range(2, 2000):
	if is_prime(i):
		primes.append(i)

print(primes)
print(len(primes))

max_chain = 0
for i in range(len(primes)):
	b = primes[i]
	if b > 1000:
		break
	for j in range(len(primes)):
		a = primes[j] - b - 1
		if abs(a) > 1000:
			continue
		n = 2
		while is_prime(n**2 + a * n + b):
			n += 1
		length = n - 1
		if length > max_chain:
			max_chain = length
			print('max_chain = %d, a = %d, b = %d' % (max_chain, a, b))

print(-61 * 971)