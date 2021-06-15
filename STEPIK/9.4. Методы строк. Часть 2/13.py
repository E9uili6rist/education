s = input()
x = 0
y = ''
for i in s:
    if s.count(i) >= x:
        x = s.count(i)
        y = i
print(y)