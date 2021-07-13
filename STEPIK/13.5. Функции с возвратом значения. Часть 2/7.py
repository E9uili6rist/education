def is_palindrome(text):
    s0 = [',', ' ', '.', '!', '?', '-']
    s = []
    for i in text:
        if i not in s0:
            s.append(i.lower())
    if s == s[::-1]:
        return True
    else:
        return False


txt = input()

print(is_palindrome(txt))