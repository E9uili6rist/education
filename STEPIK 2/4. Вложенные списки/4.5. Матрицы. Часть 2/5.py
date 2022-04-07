n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (i == j) or (i == n - 1 - j):
            print(matrix[n - 1 - i][j], end=' ')
        else:
            print(matrix[i][j], end=' ')
    print()
