my_array = [[3, 4, 5, 6, 2, 5], [2, 4, 6, 2, 5, 7], [2, 5, 7, 8, 9, 3], [2, 4, 7, 3, 5, 8], [6, 4, 7, 3, 5, 7]]

top = 0
bottom = len(my_array)-1

first_col = 0
last_col = len(my_array[0])-1

dirct = 0

while (top <= bottom and first_col <= last_col):
        if dirct==0:
            for i in range(first_col,last_col+1):
                print my_array[top][i]
            top += 1
            dirct = 1
        elif dirct == 1:
            for i in range(top,bottom+1):
                print my_array[i][last_col]
            last_col = last_col -1
            dirct = 2
        elif dirct == 2:
            for i in range(last_col,first_col-1,-1):
                print my_array[bottom][i]
            bottom = bottom - 1
            dirct = 3
        elif dirct == 3:
            for i in range(bottom,top-1,-1):
                print my_array[i][first_col]
            first_col += 1
            dirct = 0


