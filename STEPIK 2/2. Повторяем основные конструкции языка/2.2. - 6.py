sp = []
for _ in range(int(input())):
    sp.append(int(input()))
proiz = int(input())

for i in range(len(sp)):
    for j in sp:
        if i != sp.index(j):
            if sp[i] * j == proiz:
                print('ДА')
                exit(0)
            else:
                continue

print('НЕТ')