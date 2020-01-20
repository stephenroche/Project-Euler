from math import sqrt

def sum_of_factors(n):
	sum = 0
	for f in range(1, int(sqrt(n)) + 1):
		if n % f == 0:
			sum += f + n // f
	return sum - n


sums = [-1] * 1000000
marker = 1
chain_length = 0
chain = []
while marker < 1000000:
	if chain_length == 0:
		if sums[marker] != -1:
			marker += 1
			# if marker % 100 == 0:
			# 	print('marker =', marker)
			continue
		else:
			current = marker
	
	# print('current =', current)
	# print('chain_length =', chain_length)
	# print('sums[current] =', sums[current])
	chain.append(current)

	if sums[current] == -1:
		sums[current] = sum_of_factors(current)
	current = sums[current]
	chain_length += 1
	if chain_length > 100:
		print('current =', current)
		print('chain_length =', chain_length)


	if current < marker or current >= 1000000:
		# print('dead end')
		chain_length = 0
		chain = []

	elif current == marker or current in chain:
		print('chain found starting at %d, length = %d' % (current, chain_length))
		print(chain)
		print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		print()
		chain_length = 0
		chain = []
		# break
