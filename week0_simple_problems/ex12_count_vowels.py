def count_vowels(str):
    vowels_list=['a','e','i','o','u','y']
    count=0
    for character in str:
        #print ("character=",character)
        for letter in vowels_list:
            #print("letter=",letter.upper())
            if character==letter or character==letter.upper():
                count+=1
    return count
def main():
    print (count_vowels("Python"))
    print(count_vowels("Theistareykjarbunga"))
    print(count_vowels("grrrrgh!"))
    print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
    print(count_vowels("A nice day to code!"))
if __name__ == '__main__':
    main()
