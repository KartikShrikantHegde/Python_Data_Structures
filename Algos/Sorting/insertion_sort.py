def insertion_sort(my_arr):
    for i in range(1,len(my_arr)):
        current_val = my_arr[i]
        position = i

        while position > 0 and my_arr[position-1] > current_val:
            my_arr[position] = my_arr[position-1]
            position -= 1

        my_arr[position] = current_val

my_arr=[5,4,1]
insertion_sort(my_arr)
print my_arr