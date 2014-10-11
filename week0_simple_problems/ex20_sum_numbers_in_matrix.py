def sum_matrix(m):
    sum=0
    for matrix_list in m:
        for inner_list in matrix_list:
            sum+=inner_list
    return sum

print (sum_matrix([[1,2,3],[4,5,6],[7,8,9]]))
print (sum_matrix([[0,0,0],[0,0,0],[0,0,0]]))
print (sum_matrix([[1,2],[3,4],[5,6],[7,8],[9,10]]))
