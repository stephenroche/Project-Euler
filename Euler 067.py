f = open("Euler 067 triangle.txt", "r")

triangle = f.read()

triangle = triangle.split('\n')
size = len(triangle)

for y in range(size):
	triangle[y] = triangle[y].split()

for y in range(size):
	for x in range(len(triangle[y])):
		triangle[y][x] = int(triangle[y][x])

print(triangle)

totals = []
for y in range(1, size + 2):
	totals += [[0] * y]

print(totals)

for y in range(size - 1, -1, -1):
	for x in range(len(triangle[y])):
		totals[y][x] = triangle[y][x] + max(totals[y + 1][x], totals[y + 1][x + 1])

print(totals)
print(totals[0][0])