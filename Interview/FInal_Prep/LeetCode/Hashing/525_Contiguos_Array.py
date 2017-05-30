def findMaxLength(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_len = 0
    count = 0
    table = {0:0}

    for index, num in enumerate(nums,1):
        if num == 0:
            count -= 1
        else:
            count += 1

        if count in table:
            max_len = max(max_len, index - table[count])
        else:
            table[count] = index

    return max_len

print findMaxLength(nums=[0,1])