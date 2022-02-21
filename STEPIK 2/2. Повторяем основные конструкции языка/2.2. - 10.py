n = int(input())
count1 = 5
for i in range(1, n+1):
    count2 = 0
    x = input()
    for j in 'anton':
        if j in x:
            count2 += 1
            x = x[x.find(j):]
    if count1 == count2:
        print(i, end=' ')