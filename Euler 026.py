# print(7*)

import math

def is_prime(n):
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

def length_of_recursion(n):
	i = 1
	while (10**i - 1) % n != 0:
		i += 1
	return i

print(length_of_recursion(3))
print(length_of_recursion(11))
print(length_of_recursion(37))

max = 0
for i in range(7, 1000):
	if is_prime(i):
		length = length_of_recursion(i)
		if length > max:
			max = length
			print(i, length, 1 / i)
print(1/13)
print(1/999999)
print(999999/13)
print(9999999999999999999%17)