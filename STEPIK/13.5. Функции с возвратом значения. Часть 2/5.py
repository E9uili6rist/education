def is_password_good(password):
    x = password

    numbers = "1234567890"

    if len(x) < 8:
        return False
    if len([i for i in x if i == i.lower() and i not in numbers]) == 0:
        return False
    if len([i for i in x if i == i.upper() and i not in numbers]) == 0:
        return False
    if len([i for i in x if i in numbers]) == 0:
        return False
    return True


txt = input()

print(is_password_good(txt))