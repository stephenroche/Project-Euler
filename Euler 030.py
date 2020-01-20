def sum_of_digits_5(n):
	sum = 0
	for digit in str(n):
		sum += int(digit)**5
	return sum

# print(sum_of_digits_5(399999))

sum = 0
for n in range(10, 400000):
	if n == sum_of_digits_5(n):
		print(n)
		sum += n

print(sum)