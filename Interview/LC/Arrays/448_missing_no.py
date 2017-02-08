def missing_no(my_array):
    my_arr = sorted(my_array)

    start_no = 1
    if start_no not in my_arr:
        print start_no

    for i in range(0,len(my_arr)):
        if my_arr[i] - start_no != 0 and my_arr[i] - start_no != 1:
            for j in range(start_no+1,my_arr[i]):
                print j
        start_no = my_arr[i]

missing_no(my_array=[7,3,3,1])

# # LeetCode solution
#
#
#
# def missing_no(nums):
#     for i in range(len(nums)):
#         index = abs(nums[i]) - 1
#         nums[index] = - abs(nums[index])
#
#     return [i + 1 for i in range(len(nums)) if nums[i] > 0]
#
# nums = [4,3,2,7,8,2,3,1,9]
# print missing_no(nums)