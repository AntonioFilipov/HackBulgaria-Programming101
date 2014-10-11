def nth_fib_lists(listA, listB, n):
    flag = []
    if n < 1 or len(listA) == 0 and len(listB) == 0:
        return []
    elif n == 1:
        return listA
    elif n == 2:
        return listB
    for i in range(n - 2):
        flag = listA + listB
        listA = listB
        listB = flag
    return flag

print (nth_fib_lists([1], [2], 1))
print (nth_fib_lists([1], [2], 2))
print (nth_fib_lists([1, 2], [1, 3], 3))