def max_min(my_array):

    if len(my_array) == 0:
        return None


    my_min = my_array[0]
    my_max = my_array[0]

    for i in range(0,len(my_array)/2):
        num1 = my_array[i * 2]
        num2 = my_array[(i*2) + 1]

        if num1 > num2:
            if num1 > my_max:
                my_max = num1
            elif num2 < my_min:
                my_min = num2
        elif num2 > num1:
            if num2 > my_max:
                my_max = num2
            elif num1 < my_min:
                my_min = num1

    # For odd no of elements, last no would have been ommitted


    last_num = my_array[len(my_array)-1]
    if last_num > my_max:
        my_max = last_num
    elif last_num < my_min:
        my_min = last_num

    print my_max, my_min


max_min(my_array=[3,6,4,1,5,1])