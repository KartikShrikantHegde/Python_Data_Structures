# Declaring and initilazing 2d array

my_2d_array = [[0 for x in range(6)] for x in range(3)]
print my_2d_array
# for j in range(0,6):
#     my_array = [int(i) for i in raw_input().strip().split()]
#     for k in range(0,6):
#         my_2d_array[j][k] = my_array[k]
#
# print my_2d_array


# rows =3
# columns= 2
# mylist = [[1,2,3],[2,8,11],[11,10,9]]
# print mylist
# for i in range(rows):
#     for j in range(columns):
#         mylist[i][j] = '%s,%s'%(i,j)
# print mylist


'''import numpy
numpy.zeros((5,5))'''
'''
Matrix = [[0 for x in range(5)] for x in range(5)]


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
print arr'''






'''

max_val = -100
for i in range(0,4):
    for j in range(0,4):
        count = 0
        count = arr_2_d[i][j] + arr_2_d[i][j+1] + arr_2_d[i][j+2] + arr_2_d[i+1][j+1] + arr_2_d[i+2][j] + arr_2_d[i+2][j+1] + arr_2_d[i+2][j+2]
        if(count >= max_val):
            max_val = count

print max_val'''