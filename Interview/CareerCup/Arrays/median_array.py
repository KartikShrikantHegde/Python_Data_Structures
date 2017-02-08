# def median_array():
#     my_arr = [40,20,60]
#     my_arr1 = [200,400,100,800]
#
#     sorted_array1 = sorted(my_arr)
#     sorted_array2 = sorted(my_arr1)
#
#     print sorted_array1[len(my_arr)/2]
#
#     print (sorted_array2[len(sorted_array2)/2-1] + sorted_array2[len(sorted_array2)/2]) /2
#
# median_array()

array = [0, 0, 0, 1, 1, 1, 0, 0, 0]

index = len(array) - 1
for i in xrange(len(array)):
    if array[i] == 0:
        while array[index] == 0:
            index -= 1
            if i == index:
                break
        array[i] = array[index]
        array[index] = 0
        index -= 1
    print array
    if i == index:
        break

print array
