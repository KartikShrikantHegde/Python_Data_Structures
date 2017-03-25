def lss(my_arr):
    local_sum = 0
    max_sum = 0

    for i in range(0,len(my_arr)):
        local_sum = max(local_sum+my_arr[i],my_arr[i])
        max_sum = max(local_sum,max_sum)

    return max_sum


print lss(my_arr=[])