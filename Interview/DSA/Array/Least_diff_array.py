def min_diff(my_array):
    my_array.sort()
    min_val = my_array[(len(my_array)-1)] - my_array[0]
    for i in range(1,len(my_array)):
        temp_diff = abs(my_array[i]-my_array[i-1])
        if temp_diff == 0:
            return 0
        else:
            if temp_diff < min_val:
                min_val = temp_diff
    return min_val

my_array = [741,100,20,29,45,800]
print min_diff(my_array)