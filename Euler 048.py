sum = 0
for i in range(1, 1001):
	if i % 10 == 0:
		print(i)
	sum += i**i

print(sum)
print(sum % 10000000000)