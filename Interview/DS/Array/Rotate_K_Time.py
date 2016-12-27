def Roate_K_Time(my_array, k):
    for i in range(0, k):
        temp = my_array.pop(0)
        my_array.append(temp)

    return my_array


my_array = [4, 2, 3, 9, 11, 12]
print Roate_K_Time(my_array, 3)
