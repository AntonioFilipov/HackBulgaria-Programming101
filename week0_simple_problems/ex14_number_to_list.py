def number_to_list(n):
    digit_list=[]
    string_number=str(n)
    for i in range(0,len(string_number)):
        digit_list.append(string_number[i])
    return digit_list

print (number_to_list(123))
print(number_to_list(99999))
print(number_to_list(123023))

