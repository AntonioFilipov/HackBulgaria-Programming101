import sys


def cat(filename):
    my_file = open(filename, "r")
    result = my_file.read()
    my_file.close()
    return result


def main():
    print (cat(sys.argv[1]))
if __name__ == '__main__':
    main()
