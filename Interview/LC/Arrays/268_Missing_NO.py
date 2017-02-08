def missing_no(my_arr):
    total_nos = len(my_arr) + 1
    n = total_nos
    actual_sum = n * (n+1) / 2
    my_sum = sum(my_arr)

    missing_no_is = actual_sum - my_sum
    print missing_no_is


missing_no(my_arr=[1,2,3,5,6,7])