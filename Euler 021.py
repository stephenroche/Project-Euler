sum_of_divisors = [0] * 50000

for n in range (1, 10000):
	sum = 0
	for f in range(1, n // 2 + 1):
		if (n % f == 0):
			sum += f
	sum_of_divisors[n] = sum

print(sum_of_divisors)

sum = 0

for n in range (1, 10000):
	if sum_of_divisors[sum_of_divisors[n]] == n and n != sum_of_divisors[n]:
		sum += n
		print(n)

print(sum)