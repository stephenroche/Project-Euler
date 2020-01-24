from itertools import permutations

primes = [0, 0, 2, 3, 5, 7, 11, 13, 17]

sum = 0
for number in permutations(range(10)):
	i = 8
	while i >= 2:
		if (100 * number[i - 1] + 10 * number[i] + number[i + 1]) % primes[i] != 0:
			break
		i -= 1
	else:
		number = eval(str(number).replace(', ', ''))
		print(number)
		sum += number

print(sum)