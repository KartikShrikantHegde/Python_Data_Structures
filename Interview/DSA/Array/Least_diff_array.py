def min_diff(my_array):
    my_array.sort()
    min_val = max(my_array)
    for i in range(0,len(my_array)-1):
        temp_diff = abs(my_array[i]-my_array[i+1])
        if temp_diff == 0:
            return 0
        else:
            if temp_diff < min_val:
                min_val = temp_diff
    return min_val

my_array = [7,10,3,15,20,29,25,6,7]
print min_diff(my_array)