def equilibrium_arr(my_arr):
    left = 0
    right = len(my_arr) - 1
    left_sum = 0
    right_sum = 0

    while left < right:
        if left_sum <= right_sum:
            left_sum += my_arr[left]
            left += 1
        else:
            right_sum += my_arr[right]
            right -= 1
    return left


new_arr = [12, 1, 4, 6, 8]
print equilibrium_arr(new_arr)