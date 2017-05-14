def plus_one(digits):
    res = []
    my_str = ''
    for value in digits:
        my_str = my_str + str(value)
    my_str = int(my_str)
    my_str = my_str + 1
    my_str = str(my_str)
    for ch in my_str:
        ch = int(ch)
        res.append(ch)

    return res


print plus_one([9,9,9])