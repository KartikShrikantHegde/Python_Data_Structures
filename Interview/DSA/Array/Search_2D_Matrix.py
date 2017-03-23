def search_2d(my_array, ele):
    row = len(my_array) - 1
    col = len(my_array[0]) - 1

    current_row = 0
    current_col = col

    while current_row != row and current_col != -1:
        print my_array[current_row][current_col]
        if my_array[current_row][current_col] == ele:
            return "Found"
        elif my_array[current_row][current_col] > ele:
            print my_array[current_row][current_col]
            current_col -= 1
        else:
            current_row += 1
            print current_row

    return False

my_array = [[5, 7, 8, 9], [6, 9, 11, 13], [ 7, 11, 12, 14 ], [8, 13, 16, 17]]
print search_2d(my_array,6)