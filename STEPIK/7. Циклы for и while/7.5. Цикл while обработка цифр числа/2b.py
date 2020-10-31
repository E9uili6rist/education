num = 1112111
num = str(num)
res = 'YES'
for i in num:
    if num[0] != i:
        res = 'NO'
print(res)
