sum1 = 0
sum2 = 1
sum3 = 0
while sum2 < 4000000:
    sum2 = sum1 + sum2
    if sum2 % 2 == 0:
        sum3 += sum2
    sum2, sum1 = sum1, sum2
print(sum3)