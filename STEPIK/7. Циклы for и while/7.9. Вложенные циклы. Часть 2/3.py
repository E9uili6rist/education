a = 1
b = 100
summ = 0
maxsumm = 0
maxnum = 0
for i in range(a, b+1):
    for j in range(1, i+1):
        if i%j == 0:
            summ+=j
    if summ >= maxsumm:
        maxsumm = summ
        maxnum = j
    summ = 0
print(maxnum, maxsumm, end ='')