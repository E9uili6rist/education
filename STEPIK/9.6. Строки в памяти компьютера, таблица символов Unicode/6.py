n = int(input()) % 26
s = input()
s2 = ''
for i in s:
    if ord(i) - n < 97:
        decoded = chr(123 - (n - (ord(i) - 97)))
        s2 += decoded
    else:
        decoded = chr(ord(i) - n)
        s2 += decoded
print(s2)