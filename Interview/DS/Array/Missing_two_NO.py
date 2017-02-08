import math

def missing_no(my_arr, con):

    my_sum = 0
    my_squared_sum = 0
    total_sum = ((con)*(con+1))/2
    total_square_sum = ((con)*(con+1)*((2*con)+1))/6

    for i in range(0,len(my_arr)):
        my_sum = my_sum + my_arr[i]
        my_squared_sum = my_squared_sum + (my_arr[i]*my_arr[i])

    xplusy = total_sum - my_sum
    xsqaureplusysquare = total_square_sum - my_squared_sum
    twoxy = ((xplusy * xplusy) - xsqaureplusysquare)
    xminusy = math.sqrt(xsqaureplusysquare-twoxy)

    x = (xplusy + xminusy)/2
    y = (xplusy - xminusy)/2
    return x,y


my_arr = [1,3,4]
con = 5
print missing_no(my_arr,con)