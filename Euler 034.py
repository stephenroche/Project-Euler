factorials = [1]

for i in range(1, 10):
	factorials += [i * factorials[i - 1]]

print(factorials)

def sum_of_factorials(n):
	sum = 0
	for digit in str(n):
		sum += factorials[int(digit)]
	return sum

sum = 0
for n in range(3, 7 * factorials[9]):
	if n == sum_of_factorials(n):
		print(n)
		sum += n

print(sum)