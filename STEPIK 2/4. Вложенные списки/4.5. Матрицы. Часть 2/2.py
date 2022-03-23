n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
a, b = 0, 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > matrix[a][b]:
            a, b = i, j

print(a, b)