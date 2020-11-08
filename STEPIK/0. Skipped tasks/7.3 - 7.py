from math import *

n = 10
total = 0
for i in range(n):
    total += 1/(i+1)
res = total - log(n)
print(res)