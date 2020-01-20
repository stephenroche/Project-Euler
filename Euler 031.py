coins = [200, 100, 50, 20, 10, 5, 2, 1]

def combinations(total, coins, answer):
	if total == 0:
		print(answer)
		return 1

	sum = 0
	for i in range(len(coins)):
		if coins[i] <= total:
			sum += combinations(total - coins[i], coins[i:], answer + [coins[i]])

	return sum

print(combinations(1, coins, []))
print(combinations(5, coins, []))
print(combinations(10, coins, []))
print(combinations(200, coins, []))