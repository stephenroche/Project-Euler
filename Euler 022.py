f = open("Euler 022 names.txt", "r")

names = f.read()
names = names.replace('"', '')
names = names.split(',')
names.sort()

# print(names)

def score(name):
	sum = 0
	for letter in name:
		sum += (ord(letter) - ord('A') + 1)
	return sum

sum = 0
for i in range(len(names)):
	sum += (i + 1) * score(names[i])
	
# print(score('COLIN'))
print(sum)