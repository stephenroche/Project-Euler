for denominator in range(10, 100):
	if denominator % 10 == 0 or denominator % 10 == denominator // 10:
		continue

	for numerator in range(10, denominator):
		if numerator % 10 == 0 or numerator % 10 == numerator // 10:
			continue

		if numerator // 10 == denominator % 10 and (numerator % 10) / (denominator // 10) == numerator / denominator:
			print(numerator, '/', denominator)

		if numerator % 10 == denominator // 10 and (numerator // 10) / (denominator % 10) == numerator / denominator:
			print(numerator, '/', denominator)

print(1 * 2 * 1 * 4, '/', 4 * 5 * 5 * 8)