n = 192
total = 0
while n > 9:
    while n > 0:
        last_digit = n % 10
        total += last_digit
        x = total
        n = n // 10
    n = n // 10
print(total)