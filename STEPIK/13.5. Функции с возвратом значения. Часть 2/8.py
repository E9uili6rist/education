def is_valid_password(password):
    password = password.split(":")

    if len(password) != 3:
        return False

    a = password[0]
    b = password[1]
    c = password[2]

    if a != a[::-1]:
        return False

    if int(b) < 1:
        return False
    for i in range(2, int(b)):
        if int(b) % i == 0:
            return False

    if int(c) % 2 != 0:
        return False

    return True


psw = input()

print(is_valid_password(psw))