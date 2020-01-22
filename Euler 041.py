from itertools import permutations
from math import sqrt

def is_prime(n):
	if n % 2 == 0 and n != 2:
		return False
	for i in range(3, int(sqrt(n)) + 1, 2):
		if n % i == 0:
			return False
	return n > 1

def list_to_int(l):
	sum = 0
	for i in range(len(l)):
		sum += 10**i * l[-1 - i]
	return sum

# print(list_to_int([5,6,7]))

for number in permutations(range(7, 0, -1)):
	number = list_to_int(number)
	if is_prime(number):
		print(number)
		# break
