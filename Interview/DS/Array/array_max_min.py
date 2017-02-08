def max_min(my_array):
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

        # For odd no of elements

        if i * 2 < len(my_array):
            num = my_array[i*2]
            if num > my_max:
                my_max = num
            elif num < my_min:
                my_min = num


    print my_max, my_min



max_min(my_array=[3,6,4,1,8,5,1])