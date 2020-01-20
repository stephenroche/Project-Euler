def isPalindrome(n):
	n = str(n)
	return n == n[::-1]

for a in range(999, 900, -1):
	for b in range(999, 900, -1):
		n = a * b
		if isPalindrome(n):
			print('%d = %d * %d' % (n , a, b))


