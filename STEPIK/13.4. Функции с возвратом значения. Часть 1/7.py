s = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_days(month):
    return s[month - 1]

num = int(input())

print(get_days(num))