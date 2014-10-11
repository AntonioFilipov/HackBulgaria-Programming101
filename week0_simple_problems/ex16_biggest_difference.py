import math
def biggest_difference(arr):
    minimum=arr[0]-arr[1]
    


    for i in arr:
        for j in arr:
            if i!=j:
                heap_minimum=i-j
                #print ("heap_minimum",heap_minimum)
                if heap_minimum<minimum:
                    minimum=heap_minimum
    return minimum
print(biggest_difference([1,2]))
print(biggest_difference([1,2,3,4,5]))
print(biggest_difference([-10,-9,-1]))
print(biggest_difference(range(100)))
