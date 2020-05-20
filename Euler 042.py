f = open('Euler 042 words.txt', 'r')
words = f.read()

words = words.replace('"', '')
words = words.split(',')
print(words)

def word_score(word):
	sum = 0
	for letter in word:
		sum += ord(letter) - ord('A') + 1
	return sum

print(max([word_score(word) for word in words]))

triangulars = [n * (n + 1) // 2 for n in range(1, 21)]
print(triangulars)

n_words = 0
for word in words:
	if word_score(word) in triangulars:
		n_words += 1

print(n_words)