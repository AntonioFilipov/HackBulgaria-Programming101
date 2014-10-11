def group_by(func, seq):
    my_dictionary = {}
    
    for item in seq:
        key = func(item)
        if key in my_dictionary:
            my_dictionary[key].append(item)
        else:
            my_dictionary[key] = [item]
    return my_dictionary

print (group_by(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))
