def is_double_palindrome(n):
	n_dec = str(n)
	n_bin = bin(n)[2:]

	for i in range(len(n_dec) // 2):
		if n_dec[i] != n_dec[-1 - i]:
			return False

	for i in range(len(n_bin) // 2):
		if n_bin[i] != n_bin[-1 - i]:
			return False

	return True

sum = 0
for n in range(1000000):
	if is_double_palindrome(n):
		print(n, bin(n)[2:])
		sum += n

print(sum)