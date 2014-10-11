def nan_expand(times):
    if times == 0:
        return ""
    nan_string = "Not a "
    result_string = ""
    for i in range(1, times + 1):
        result_string += nan_string


    return (result_string + " NaN")
print (nan_expand(0))
print (nan_expand(1))
print (nan_expand(2))
print (nan_expand(3))
