from ex15_list_to_number import list_to_number
def zero_insert(n):
    number_list=[]
    for i in str(n):
        number_list.append(i)
    for digit in range(1,len(number_list)):
        if number_list[digit-1]==number_list[digit] or (int(number_list[digit-1])+int(number_list[digit]))%10==0:
            number_list.insert(digit,'0')
    return list_to_number(number_list)
def main():
    print (zero_insert(116457))
    print (zero_insert(55555555555))
    print (zero_insert(1))
    print (zero_insert(6446))
if __name__ == '__main__':
    main()

