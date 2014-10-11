from ex12_count_vowels import count_vowels
def count_consonants(str):
    count=0
    for i in str:
        if i==' ' or i=='!' or i=='.' or i==','or i=='?':
            count+=1
    return (len(str)-(count_vowels(str)+count))

def main():
    print(count_consonants("Python"))
    print(count_consonants("Theistareykjarbunga"))
    print(count_consonants("grrrrgh!"))
    print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
    print(count_consonants("A nice day to code!"))
if __name__ == '__main__':
    main()