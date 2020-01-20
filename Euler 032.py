from itertools import permutations

products = set()

for digits in permutations([i for i in range(1, 10)], 5):
	a = 10 * digits[0] + digits[1]
	b = 100 * digits[2] + 10 * digits[3] + digits[4]
	product = a * b
	if product >= 10000:
		continue
	
	product_digits = [int(x) for x in str(product)]
	for i in range(4):
		if product_digits[i] == 0 or product_digits[i] in digits or product_digits[i] in product_digits[i + 1:]:
			break
	else:
		print(a, b, product)
		products.add(product)

print(products)
print(sum(products))



for digits in permutations([i for i in range(1, 10)], 5):
	a = digits[0]
	b = 1000 * digits[1] + 100 * digits[2] + 10 * digits[3] + digits[4]
	product = a * b
	if product >= 10000:
		continue
	
	product_digits = [int(x) for x in str(product)]
	for i in range(4):
		if product_digits[i] == 0 or product_digits[i] in digits or product_digits[i] in product_digits[i + 1:]:
			break
	else:
		print(a, b, product)
		products.add(product)

print(products)
print(sum(products))