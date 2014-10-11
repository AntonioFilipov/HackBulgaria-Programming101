def count_substrings(haystack, needle):
    count = 0
    flag = 0
    main_count = 0
    for i in range(0, len(haystack)):
        #print("i=",i)
        for j in range(flag, len(needle)):
            #print ("j=",j)
            if haystack[i] == needle[j]:
                count += 1
               # print ("count=",count)
                flag += 1
                #print ("flag in if=",flag)
                if count == int(len(needle)):
                    main_count += 1
                    #print ("main_count",main_count)
                    count = 0
                    #print ("count in if if=",count)
                    flag = 0
                    #print ("flag in if if=",flag)

            break
    return main_count


def main():
    print (count_substrings("This is a test string", "is"))
    print (count_substrings("babababa", "baba"))
    print (count_substrings("Python is awesome language to program in!", "o"))
    print (count_substrings("We have nothing in common!", "really?"))
    print (count_substrings("This is this and that is this", "this"))
if __name__ == '__main__':
    main()
