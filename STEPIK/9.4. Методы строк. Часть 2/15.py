s = input()
x = s.find('h')
y = s.rfind('h')
print(s[0:x], s[y+1:], sep='')