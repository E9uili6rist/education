def get_next_prime(num):
    if num == 1:
        return 2
    x = num
    while num > 0:
        count = 0
        for i in range(1, x+1):
            if x % i == 0:
                count += 1
        if count == 2 and x > num:
            return x
        else:
            x += 1

n = int(input())

print(get_next_prime(n))