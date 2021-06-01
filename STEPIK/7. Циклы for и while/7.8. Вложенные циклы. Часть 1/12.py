import math
for a in range(1, 151):
    for b in range(1, 151):
        for c in range(1, 151):
            for d in range(1, 151):
                equation = a ** 5 + b ** 5 + c ** 5 + d ** 5
                e = math.pow(equation, 1/5)
                if int(e) ** 5 == equation:
                    print(a, b, c, d, e)