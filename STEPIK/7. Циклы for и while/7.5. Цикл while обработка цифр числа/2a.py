num = int(11111111)
last_digit1 = num % 10
same = True # сигнальная метка
while num != 0:
    last_digit2 = num % 10
    if last_digit1 / last_digit2 != 1:
        same = False
    num = num // 10
if same == True:
    print('YES')
else:
    print('NO')