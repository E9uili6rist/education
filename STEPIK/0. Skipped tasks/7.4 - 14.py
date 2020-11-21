n = 25
coins = 0
while n > 0:
    if n - 25 >= 0:
        n -= 25
        coins += 1
    elif n - 10 >= 0:
        n -= 10
        coins += 1
    elif n - 5 >= 0:
        n -= 5
        coins += 1
    elif n - 1 >= 0:
        n -= 1
        coins += 1
print(coins)