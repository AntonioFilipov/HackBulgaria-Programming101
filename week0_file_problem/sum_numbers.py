import sys

def sum_numbers(filename):
    my_file = open(filename, "r")
    numbers = my_file.read().split(" ")
    my_file.close()
    sum = 0
    for item in numbers:
        if len(item) > 0:
            sum += int(item)
    return sum

def main():
    print (sum_numbers(sys.argv[1]))
if __name__ == '__main__':
    main()
