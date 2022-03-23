n = int(input())
matrix = []
elements = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

for c in range(len(matrix)):
    for d in range(c + 1):
        elements.append(matrix[c][d])

print(max(elements))