def is_number_balanced(n):
    list_digit = []
    right_sum = 0
    left_sum = 0
    while(n != 0):
        digit = n % 10
        list_digit.append(digit)
        n //= 10
    if len(list_digit) % 2 == 0:
        for i in range(0, int(len(list_digit) / 2)):
            right_sum += list_digit[i]
        for i in range(int(len(list_digit)/2), int(len(list_digit))):
            left_sum += list_digit[i]

    if len(list_digit) % 2 == 1:
        for i in range(0, int(len(list_digit) / 2)):
            right_sum += list_digit[i]

        for i in range(int(len(list_digit)/2+1), int(len(list_digit))):
            left_sum += list_digit[i]

    if right_sum == left_sum:
        return True
    return False


def main():
    print(is_number_balanced(9))
    print(is_number_balanced(11))
    print(is_number_balanced(13))
    print(is_number_balanced(121))
    print(is_number_balanced(4518))
    print(is_number_balanced(28471))
    print(is_number_balanced(1238033))
if __name__ == '__main__':
    main()



