n = int(input())
s = []
for i in range(1, n+1):
    s.append(input())
x = input()
for num in s:
    if x.lower() in num.lower():
        print(num)