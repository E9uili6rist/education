s = input()
count = 0
for i in s:
    if i == 'f':
        count += 1
if count == 1:
    print(s.find('f'))
elif count > 1:
    print(s.find('f'), s.rfind('f'))
elif count == 0:
    print('NO')