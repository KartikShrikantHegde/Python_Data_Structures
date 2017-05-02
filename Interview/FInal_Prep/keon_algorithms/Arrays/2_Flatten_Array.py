
def flatten(array, result):
    for i in array:
        if type(i) == type([]):
            flatten(i, result)
        else:
            result.append(i)
    return result


my_arr = [1,[3,4]]
res = []
print flatten(my_arr,res)
