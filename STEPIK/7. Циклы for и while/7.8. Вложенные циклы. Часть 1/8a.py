n = 5
kol = 1
for i in range(1,n+1):
  if n/i > 2:
    print('*'*kol)
    kol+=1
  else:
    print('*'*kol)
    kol-=1