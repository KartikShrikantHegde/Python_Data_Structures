def selection_sort(my_array):
    for i in range(0,len(my_array)):
        least_val = i

        for j in range(i+1,len(my_array)):
            if my_array[j] < my_array[least_val]:
                least_val = j

        swap(my_array,least_val,i)

def swap(new_arr,i,j):
    temp = new_arr[i]
    new_arr[i] = new_arr[j]
    new_arr[j] = temp

my_array=[4,3,8,2,1]
print "Before - ", my_array
selection_sort(my_array)
print"after  - " , my_array