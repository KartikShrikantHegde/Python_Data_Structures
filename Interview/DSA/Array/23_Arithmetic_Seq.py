def Arithmetic_Seq(my_array):
    count = 0
    prev_diff = 0
    max_count = 0
    for i in range(1, len(my_array)):
        if i == 1:
            prev_diff = my_array[i] - my_array[0]
            count = max_count = 2
            continue

        x = my_array[i] - my_array[i - 1]
        if prev_diff == x:
            count += 1
            max_count = count
        else:
            count = 2
            prev_diff = x
    return max_count


print Arithmetic_Seq(my_array=[2,5,8,3,4,8,9,11,12, 15, 34, 23,24,25,26])
