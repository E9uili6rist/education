n = int(input())
sum = 0
for i in range(1, n+1):
    multi = 1
    for j in range(1, i+1):
        multi = multi * j
    sum += multi
print(sum)