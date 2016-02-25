# Smallest no in list

def smallest(my_array):

    smallest = my_array[0]
    for i in my_array:
        if i < smallest:
            smallest= i
    return smallest


my_array = [9, 41, 12, 3, 74, 15,5]
print smallest(my_array)
