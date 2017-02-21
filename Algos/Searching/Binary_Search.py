''' Time complexity -> log(n). At each step half of the elements are discarded for searching '''

def binary_search(my_arr, k ):
    low = 0
    high = len(my_arr)-1

    if len(my_arr) == 0:
        print "Empty array. Cant search the element"

    while low <= high:
        mid = ( low + high ) / 2

        if k > my_arr[mid]:
            low = mid + 1
        elif k < my_arr[mid]:
            high = mid -1
        else:
            print "Found at :", mid+1, "Position"
            break

    if low > high:
        print "Nothing Found"

my_array = [2,3,4,7,8,9]
k = 9
binary_search(my_array,k)
