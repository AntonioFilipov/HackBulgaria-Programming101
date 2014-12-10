import sys
from random import randint

def generate_numbers(filename, n):
    my_file = open(filename, "w")
    for i in range(1, n):
        my_file.write(str(randint(1, 1000)) + " ")
    my_file.close()

def main():
   generate_numbers(sys.argv[1], int(sys.argv[2]))
if __name__ == '__main__':
    main()
