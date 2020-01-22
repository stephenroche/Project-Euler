from math import log10

def nth_digit(n):
	number = 0
	counter = 0
	while counter < n:
		number += 1
		counter += int(log10(number)) + 1

	# print(number, counter)
	return int(str(number)[-1 - (counter - n)])

# print(nth_digit(1))
# print(nth_digit(9))
# print(nth_digit(10))
# print(nth_digit(11))
# print(nth_digit(12))
# print(nth_digit(13))
# print(nth_digit(14))
# print(nth_digit(15))

product = 1
for power in range(6):
	product *= nth_digit(10**power)

print(product)