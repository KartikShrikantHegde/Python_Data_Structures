def sort_three(nums):
    from collections import Counter

    my_list = []
    for k , v in Counter(nums).items():
        while v != 0:
            my_list.append(k)
            v -= 1

    return my_list

print sort_three( nums = [7, 1, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0])