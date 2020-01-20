months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

first_day_of_month = 0
sum = 0

for year in range(1900, 2001):
	for month in range(12):
		if first_day_of_month == 6 and year != 1900:
			sum += 1
			print(year, month + 1)
		first_day_of_month = (first_day_of_month + months[month] + (1 if month == 1 and year % 4 == 0 and year != 1900 else 0)) % 7

print(sum)