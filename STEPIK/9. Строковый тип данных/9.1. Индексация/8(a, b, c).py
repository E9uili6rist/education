s = 'abc'
for i in reversed(range(0, len(s))):
    print(s[i])

s = 'abc'
for i in range(1, len(s) + 1):
    print(s[-i])

s = 'abc'
for i in range(-1,-len(s)-1, -1):
    print(s[i])