n = int(input())
def pascal(n):
    lst = []
    for i in range(n + 1):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j != i and j != 0: row[j] = lst[i - 1][j - 1] + lst[i - 1][j]
        lst.append(row)
    return lst[n] if n != 0 else [1]

print(pascal(n))