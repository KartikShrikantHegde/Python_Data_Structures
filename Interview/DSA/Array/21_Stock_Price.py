def Stock_Price(my_array):
    # # profit = 0
    # prev_val = my_array[0]
    # for i in range(1,len(my_array)):
    #     prev_val =  my_array[i] - my_array[i-1]
    #     if prev_val > 0:
    #         profit += prev_val
    #     else:
    #         prev_val = 0

    profit = 0
    prev_val = my_array[0]
    for i in range(0, len(my_array)):
        if my_array[i] > prev_val:
            profit += (my_array[i] - prev_val)
        prev_val = my_array[i]

    return profit


print Stock_Price(my_array=[400, 402, 435, 398])




#
# profit = 0
#     prev_val = my_array[0]
#     for i in range(0,len(my_array)):
#         if (my_array[i]>prev_val):
#             profit += (my_array[i] - prev_val)
#         prev_val = my_array[i]
#
#     return profit
