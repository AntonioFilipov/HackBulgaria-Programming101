def is_int_polindrome(n):
    reversed_list = []
    normal_list = []
    while(n != 0):
        digit = n % 10
        reversed_list.append(digit)
        n //= 10
    normal_list = reversed_list[::-1]
    if normal_list == reversed_list:
        return True
    return False


def main():
    print (is_int_polindrome(123))
if __name__ == '__main__':
    main()
