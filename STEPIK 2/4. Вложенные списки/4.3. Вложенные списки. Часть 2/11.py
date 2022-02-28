n = int(input())
lst = []
for i in range(n):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != i and j != 0: row[j] = lst[i - 1][j - 1] + lst[i - 1][j]
    lst.append(row)
for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j], end=' ')
    print()