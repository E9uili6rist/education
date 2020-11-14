n = int(input())
largest1 = -1
for i in range(n):
    num = int(input())
    if num > largest1:
        largest2 = largest1
        largest1 = num
    elif num > largest2:
        largest2 = num
print(largest1)
print(largest2)