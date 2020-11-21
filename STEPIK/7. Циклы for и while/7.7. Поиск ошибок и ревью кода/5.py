mx = -1000000
s = 0
for i in range(5):
    x = int(input())
    if x < 0:
        s = s + x
    if 0 > x > mx:
        mx = x
if s < 0:
    print(s)
    print(mx)
else:
    print("NO")