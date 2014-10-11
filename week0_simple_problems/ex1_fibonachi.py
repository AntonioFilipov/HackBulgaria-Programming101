def nth_fibonacci(n):
    a = 0
    sum = 1
    if n == 1 or n == 2:
        return 1

    for digit in range(1, n):
        b = sum
        sum = a + b
        a = b
    return sum


def main():
    print (nth_fibonacci(3))
if __name__ == '__main__':
    main()
