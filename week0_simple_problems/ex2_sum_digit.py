def sum_of_digit(n):
    sum = 0
    while (n != 0):
        digit = n % 10
        n //= 10
        sum += digit
        return sum


def main():
    print(sum_of_digit(123))
if __name__ == '__main__':
    main()
