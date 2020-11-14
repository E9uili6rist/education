amount = 3
flag = True
for i in range(amount):
    number = int(input())
    if number % 2 != 0:
        flag = False
if flag == False:
    print('NO')
else:
    print('YES')