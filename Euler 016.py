def sum_digits(n):
	sum = 0
	for digit in str(n):
		sum += int(digit)
	return sum

print(sum_digits(2**1000))