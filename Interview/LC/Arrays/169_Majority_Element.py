from collections import Counter
def majority_ele(my_arr):
    arr_len = len(my_arr)

    x = [k for k,v in Counter(my_arr).items() if v > arr_len/2]
    for i in range(len(x)):
        print x[i]

majority_ele(my_arr=[2,2])


