def rotate_vowels(my_str):
    vowels = ['a','e','i','o','u']

    my_arr = list(my_str)

    if my_arr is None or len(my_arr) == 0:
        return my_arr

    i = 0
    j = len(my_arr) - 1

    while True:
        while i < len(my_arr) and my_arr[i] not in vowels:
            i += 1

        while j >= 0 and my_arr[j] not in vowels:
            j -= 1

        if i < j:
            swap(my_arr, i, j)
            i += 1
            j -= 1
        else:
            break

    return ''.join(my_arr)


def swap(my_arr, i, j):
    temp = my_arr[i]
    my_arr[i] = my_arr[j]
    my_arr[j] = temp

print rotate_vowels(my_str='leitcode')