for n in range(1, 366):
    for k in range(1, 366):
        for m in range(1, 366):
            if n * 28 + k * 30 + m * 31 == 365:
                print('n =', n, 'k =', k, 'm =', m)