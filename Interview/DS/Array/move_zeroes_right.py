def move_zeroes_rihgt(my_array):
    start = 0
    end = len(my_array) - 1
    while start < end:
        if my_array[start] == 0 and my_array[end] != 0:
            temp = my_array[start]
            my_array[start] = my_array[end]
            my_array[end] = temp
            start += 1
            end -= 1
        else:
            if my_array[start] != 0:
                start += 1
            elif my_array[end] == 0:
                end -= 1

    print my_array


move_zeroes_rihgt(my_array=[0, 5, 0, 2, 3, 0, 3, 5, 0])
