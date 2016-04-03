# HackerRank - 2D Array problem

my_2d_array = [[0 for x in range(6)] for x in range(6)]
for j in range(0,6):
    my_array = [int(i) for i in raw_input().strip().split()]
    for k in range(0,6):
        my_2d_array[j][k] = my_array[k]

max_val = None
for i in range(0,4):
    for j in range(0,4):
        count = 0
        count = my_2d_array[i][j] + my_2d_array[i][j+1] + my_2d_array[i][j+2] + my_2d_array[i+1][j+1] + my_2d_array[i+2][j] + my_2d_array[i+2][j+1] + my_2d_array[i+2][j+2]
        if(count >= max_val):
            max_val = count

print max_val