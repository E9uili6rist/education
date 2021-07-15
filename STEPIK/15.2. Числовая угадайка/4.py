n = int(input())
count = 1
while True:
    if 2**count >= n:
        print(count)
        break
    else:
        count += 1