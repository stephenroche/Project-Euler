for i in range(6):
	print(i)

print("thanks Greta")

primes = {}
max_factor = 20
for n in range(1, 1 + max_factor):
	print('n =', n)
	factor = 2
	power = 0
	while n != 1 or power != 0:
		if n % factor == 0:
			power += 1
			n /= factor
		else:
			if power > 0 and (factor not in primes or primes[factor] < power):
				primes[factor] = power

			power = 0
			factor += 1

	print(primes)

answer = 1
for prime in primes:
	answer *= prime ** primes[prime]

print(answer)