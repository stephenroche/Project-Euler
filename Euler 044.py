def pentagonal(n):
	return n * (3 * n - 1) // 2

# # j = 1
# # while j < 100:
# # 	k = j - 1
# # 	while k > 0:


# for n in range(1, 250):
# 	print(pentagonal(n), pentagonal(n) - pentagonal(n - 1))

# #	1	3	6	10	15	21	28	36	45	55	66	78
# #	7	13	21	31	43	57	73	91	111	133

# pentagonals = set()
# n = 1
# while pentagonal(n) < 10000:
# 	pentagonals.add(pentagonal(n))
# 	n += 1

# triangular_sums = set()
# n = 1
# while n * (n + 1) // 2 + (n + 2) * (n + 3) // 2 < 10000:
# 	if n % 3 != 0:
# 		triangular_sums.add(n * (n + 1) // 2 + (n + 2) * (n + 3) // 2)
# 	n += 1

# print(pentagonals.intersection(triangular_sums))

# print(31+28+25+22+19+16+13, 34+37+40+43)

import math

pentagonals = [0, 1]
k = 1
min_D = math.inf
while k < len(pentagonals) and k < 100:
	while pentagonals[-1] < 2 * pentagonals[k]:
		pentagonals += [pentagonal(len(pentagonals))]
	# print(pentagonals[k], pentagonals)

	i = 1
	while i < k and pentagonals[i] < min_D:
		if (pentagonals[k] - pentagonals[i]) in pentagonals and (2 * pentagonals[k] - pentagonals[i]) in pentagonals:
			print('%d - %d = %d, %d + %d = %d', pentagonals[k], pentagonals[k] - pentagonals[i], pentagonals[i], pentagonals[k], pentagonals[k] - pentagonals[i], 2 * pentagonals[k] - pentagonals[i])
			min_D = pentagonals[i]
		i += 1

	k += 1