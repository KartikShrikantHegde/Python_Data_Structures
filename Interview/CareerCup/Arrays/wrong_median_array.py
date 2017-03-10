def mov_ones(my_arr):
    if my_arr is None or len(my_arr) == 0:
        return my_arr

    i = 0
    j = len(my_arr) - 1

    while i < j:
        if my_arr[i] != 0:
            i += 1
        elif my_arr[j] == 0:
            j -= 1
        else:
            swap(my_arr, i, j)

    return my_arr


def swap(my_arr, i, j):
    temp = my_arr[i]
    my_arr[i] = my_arr[j]
    my_arr[j] = temp


print mov_ones(my_arr=[0, 0, 0, 1, 1, 1, 0, 0])