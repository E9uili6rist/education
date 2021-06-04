n = int(input())
ostatok = ''
while n > 0:
    ostatok = str(n % 2) + ostatok  #для обратного порядка, если сделать ostatok = ostatok + str(n % 2), то выводиться будет в прямом порядке
    n = n // 2
print(ostatok)