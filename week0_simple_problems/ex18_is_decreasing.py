def is_increasing(seq):
    if len(seq)==1:
        return True
    flag=seq[1]-seq[0]
    for i in range(1,len(seq)):
        if seq[i]>seq[i-1]:
            return False
        if(seq[i]-seq[i-1])!=flag:
            return False
    return True
print (is_increasing([1,2,3,4,5]))
print (is_increasing([1,3,2]))
print (is_increasing([1]))
print (is_increasing([5,6,-10]))
print (is_increasing([1,1,1,1]))
print (is_increasing([5,4,3,2,1]))
print (is_increasing([1,2,3]))
print (is_increasing([100,50,20]))
print (is_increasing([1,1,1,1]))

