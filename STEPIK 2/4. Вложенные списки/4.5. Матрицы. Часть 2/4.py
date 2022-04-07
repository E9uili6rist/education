n = int(input())
matrix = []
for d in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            print('NO')
            exit(0)
else:
    print('YES')