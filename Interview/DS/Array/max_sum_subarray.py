def max_sub_array(my_array):
    max_sum = 0
    max_now = 0
    for i in range(0,len(my_array)):
        max_now = max_now + my_array[i]
        if max_now < 0:
            max_now = 0
        elif max_now > max_sum:
                max_sum = max_now

    if max_sum <= 0:
        return 5
    return max_sum

print max_sub_array(my_array=[-2, -3,10,2])