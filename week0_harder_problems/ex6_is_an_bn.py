def is_an_bn(word):
    count_a = 0
    count_b = 0

    if len(word) == 0:
        return True

    if len(word) % 2 == 1 or word[0] != 'a':
        return False

    for char in range(0, len(word)//2):
        if word[char] == 'a':
            count_a += 1
    for char in range(len(word)//2, len(word)):
        if word[char] == 'b':
            count_b += 1

    if count_a == count_b == len(word)//2:
        return True
    return False

