digits = [1, 2, 3, 5, 7, 9]

from math import sqrt, log10

def is_prime(n):
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return n > 1

def find_left_trucatable(n, s):
	if is_prime(n):
		print(n)
		s.add(n)

		for digit in digits:
			find_left_trucatable(n + digit * 10**(int(log10(n)) + 1), s)

def find_right_trucatable(n, s):
	if is_prime(n):
		print(n)
		s.add(n)

		for digit in digits:
			find_right_trucatable(10 * n + digit, s)

left_trucatable = set()
for n in range(1, 10):
	find_left_trucatable(n, left_trucatable)

right_trucatable = set()
for n in range(1, 10):
	find_right_trucatable(n, right_trucatable)

both_truncatable = left_trucatable.intersection(right_trucatable)
print(both_truncatable)
print(sum([x for x in both_truncatable if x >= 10]))