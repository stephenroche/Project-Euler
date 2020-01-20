# # print(2**100)
# # print(29**100)
# # print(99**100)

# from math import log

# def duplicates(n):
# 	sum = 0
# 	for power in range(4, 101):
# 		for factor in range(2, min(int(log(100, n)) + 1, power)):
# 			if power % factor == 0:
# 				sum += 1
# 				print('%d**%d == %d**%d' % (n, power, n**factor, power / factor))

# 	return sum

# print(duplicates(2))
# print(duplicates(8))
# print(duplicates(3))
# # print(duplicates(36))

# for n in range(2, 11):
# 	print(duplicates(n))

# # print(99 * 99 - 49 * 6 - 81)

# print(9**90 - 27**60)
# print(27**80 - 81**60)

from math import log

numbers = list(range(2,101))
sum = 0

while numbers != []:
	n = numbers[0]
	print('***n =', n)
	powers = set()
	for x in range(1, int(log(100, n)) + 1):
		print('x =', x)
		numbers.remove(n**x)
		for i in range(2, 101):
			powers.add(x * i)

	print(len(powers))
	sum += len(powers)

print(sum)