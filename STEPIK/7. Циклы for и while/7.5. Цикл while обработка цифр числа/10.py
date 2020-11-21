n = 711
largest = -1
flag = True
while n != 0:
    last_digit = n % 10
    if last_digit >= largest:
        largest = last_digit
    else:
        flag = False
    n = n // 10
if flag == True:
    print('YES')
else:
    print('NO')