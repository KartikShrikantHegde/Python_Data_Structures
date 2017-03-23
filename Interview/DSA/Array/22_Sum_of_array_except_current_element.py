def arraysum(my_arr):
    new_arr = []

    if len(my_arr) == 0:
        return my_arr

    for i in range(0, len(my_arr)):
        sum1 = 0
        sum2 = 0
        j = i + 1
        k = 0

        while j != len(my_arr):
            sum1 = sum1 + my_arr[j]
            j += 1

        while k != i:
            sum2 = sum2 + my_arr[k]
            k += 1

        new_arr.append(sum1 + sum2)

    return new_arr

my_arr = [3,-2]
print arraysum(my_arr)