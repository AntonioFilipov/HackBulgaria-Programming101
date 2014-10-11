from ex7_int_palindrom import is_int_polindrome


def next_hack(n):
    
    run_count = 0
    while(run_count == 0):
        n += 1
        count = 0
        flag = 0
        binary_number_0b = str(bin(n))
        binary_number = binary_number_0b[2: len(binary_number_0b)]
        
        for i in binary_number:
            if i == '1':
                count += 1
        if count % 2 == 1:
            flag = 1
    
        if flag == 1 and is_int_polindrome(int(binary_number)):
            run_count += 1
            return n

print (next_hack(0))
print (next_hack(10))
print (next_hack(8031))
print (next_hack(8190))


print (next_hack(456))
print (next_hack(1))

