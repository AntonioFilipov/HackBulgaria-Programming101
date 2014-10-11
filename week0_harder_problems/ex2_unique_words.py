def unique_words(arr):
    words_unique = []
    count = 0
    for word in arr:
        if not word in words_unique:
            count += 1
            words_unique.append(word)
    return words_unique


def main():
    print (unique_words(["apple", "banana", "apple", "pie"]))
    print (unique_words(["python", "python", "python", "ruby"]))
if __name__ == '__main__':
    main()
