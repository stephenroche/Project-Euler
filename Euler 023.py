def is_abundant(n):
	sum = 0
	for f in range(1, n // 2 + 1):
		if n % f == 0:
			sum += f
	return sum > n

abundants = [False] * 28124

for n in range(12, 28123):
	if is_abundant(n):
		abundants[n] = True

print(enumerate(abundants))

sum = 0
for n in range(1, 28123):
	i = 12
	while i < n:
		if abundants[i] and abundants[n - i]:
			break
		i += 1
	else:
		sum += n
		print(n)

print(sum)