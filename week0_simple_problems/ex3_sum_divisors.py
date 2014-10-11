def sum_divisors(n):
    sum = 0
    for i in range(1, n+1):
        if n % i == 0:
            sum += i
    return sum


def main():
    print (sum_divisors(1000))
if __name__ == '__main__':
    main()
