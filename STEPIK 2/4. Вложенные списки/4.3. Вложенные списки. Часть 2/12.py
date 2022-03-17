st = input()
it = 0
res = []
for i in range(2, len(st), 2):
    if st[i] != st[i-2]:
        res.append(st[it:i].split())
        it = i
res.append(st[it:].split())
print(res)