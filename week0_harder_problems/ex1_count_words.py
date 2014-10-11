def count_words(arr):
    my_dictionary = {}
    for word in arr:
        count = 0
        for counting_word in arr:
            if word == counting_word:
                count += 1
                my_dictionary[word] = count
    return my_dictionary

def main():
    print (count_words(["apple", "banana", "apple", "pie"]))
    print (count_words(["python", "python", "python", "ruby"]))
if __name__ == '__main__':
    main()
