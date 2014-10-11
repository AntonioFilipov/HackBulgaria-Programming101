def contains_digit(number, digit):
    while(number != 0):
        number_digit = number % 10
        number //= 10
        if number_digit == digit:
            return True
    return False


def main():
    print (contains_digit(123, 4))
    print (contains_digit(42, 2))
    print (contains_digit(1000, 0))
    print (contains_digit(12346789, 5))
if __name__ == '__main__':
    main()
