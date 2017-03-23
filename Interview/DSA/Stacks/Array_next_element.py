def find_next_smaller_elements(xs):
    ys=[-1 for x in xs]
    my_arr=[]
    for i,x in enumerate(xs):
        # print my_arr[-1]
        # print xs[my_arr[-1]]
        while len(my_arr)>0 and x<xs[my_arr[-1]]:
           ys[my_arr.pop()]=x
        my_arr.append(i)
    return ys

print find_next_smaller_elements([4,2,1,5,3])