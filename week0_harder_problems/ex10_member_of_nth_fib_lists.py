def member_of_nth_fib_lists(listA, listB, needle):
    flag = []
    while len(flag) < len(needle):
        flag = listA + listB
        listA = listB
        listB = flag
    if flag == needle:
        return True
    return False


def main():
    print (member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))
    print (member_of_nth_fib_lists([7, 11], [2], [7, 11, 2, 2, 7, 11, 2]))
if __name__ == '__main__':
    main()
