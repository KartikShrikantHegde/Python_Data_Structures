def move_zeroes_right(nums):
    last0 = 0
    for i in range(0, len(nums)):
        if (nums[i] != 0):
            nums[i], nums[last0] = nums[last0], nums[i]
            last0 += 1

    print my_arr

my_arr = [0,1,0,3,12]
move_zeroes_right(my_arr)