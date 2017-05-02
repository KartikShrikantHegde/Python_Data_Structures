''' Print every 3rd element in array till nothing is left'''


def circular_remove(my_arr, k):
    index = 0
    skip = k - 1

    while len(my_arr) > 0:
        index = (skip + index) % len(my_arr)
        print my_arr.pop(index)


arr = [1, 2]
k = 4
circular_remove(arr, k)
