def contains_digit(number, digit):
    while(number != 0):
        number_digit = number % 10
        number //= 10
        for i in digit:
            if number_digit == i:
                digit.remove(i)

    if len(digit) == 0:
        return True
    return False


def main():
    print (contains_digit(402123, [0, 3, 4]))
    print (contains_digit(666, [6, 4]))
    print (contains_digit(123456789, [1, 2, 3, 0]))
    print (contains_digit(456, []))
if __name__ == '__main__':
    main()
