#поиск второй цифры числа

num = int(455672)
while num > 9:
    last_digit = num % 10
    num = num // 10
print(last_digit)