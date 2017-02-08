def mov_zeroes(my_arr):
    if my_arr is None or len(my_arr) == 0:
        return my_arr

    i = 0
    j = len(my_arr) - 1

    while True:
        while i < len(my_arr) and my_arr[i] == 0:
            i+=1

        while j >= 0 and my_arr[j] != 0:
            j-=1

        if i<j:
            swap(my_arr,i,j)
        else:
            break

    return my_arr

def swap(my_arr,i,j):
    temp = my_arr[i]
    my_arr[i] = my_arr[j]
    my_arr[j] = temp

print mov_zeroes(my_arr=[0,1,0,0,0,1,1,0,1])
