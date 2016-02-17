# Find the smallest no in a list

def small():
    my_array = [9, 41, 12, 3, 74, 15,1]
    smallest = my_array[0]
    for i in my_array:
        if i < smallest:
            smallest= i
    return smallest

print small()
