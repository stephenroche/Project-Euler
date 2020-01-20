a = 0
b = 1
sum = 0

while(b < 4e6):
	print(b)
	if b % 2 == 0:
		sum += b

	a, b = b, b + a

print(sum)