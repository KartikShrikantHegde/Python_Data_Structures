def Stock_Price(my_array):
    profit = 0
    prev_val = my_array[0]
    for i in range(0,len(my_array)):
        if (my_array[i]>prev_val):
            profit += (my_array[i] - prev_val)
        prev_val = my_array[i]

    return profit


print Stock_Price(my_array = [1,2,4])