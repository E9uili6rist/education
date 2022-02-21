n = int(input())
count = 0
lst = []
if len(str(n)) <= 3:
        print(n)
if len(str(n)) > 3:
    n2 = str(n)[::-1]
    for _ in n2:
        count += 1
        lst.append(_)
        if count % 3 == 0 and _ != n2[-1]:
            lst.append(',')
print(*lst[::-1], sep='')