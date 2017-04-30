def indexof(my_arr, target):
    counter = 0
    for i in range(len(my_arr)):
        if my_arr[i] == target:
            break
        else:
            counter += 1

    return counter


my_arr = [20, 10, 40, 30, 50]

target = 40

print indexof(my_arr, target)
