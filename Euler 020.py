def sum_digits(n):
	sum = 0
	for digit in str(n):
		sum += int(digit)
	return sum

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

print(sum_digits(factorial(100)))