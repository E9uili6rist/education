def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    count = 0
    for i in range(0, len(word1)):
        if word1[i] == word2[i]:
            count += 1

    if len(word1) - count == 1:
        return True
    else:
        return False


txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))