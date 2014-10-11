
def is_prime(n):
    if n == 1 or n <= 0:
        return False
    if n == 2:
        return True

    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True


def main():
    print (is_prime(-10))
if __name__ == '__main__':
    main()
