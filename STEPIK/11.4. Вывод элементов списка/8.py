n = int(input())
s1 = []
s2 = []
s3 = []
for i in range(1, n+1):
    x = int(input())
    if x<0:
        s1.append(x)
    elif x == 0:
        s2.append(x)
    elif x > 0:
        s3.append(x)
s1.extend(s2)
s1.extend(s3)
print(*s1, sep='\n')