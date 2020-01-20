sum = 1
size = 1001
for n in range(2, size // 2 + 2):
	sum += 4 * (4 * n**2 - 7 * n + 4)
print(sum)