def max_prod_sub_array(my_array):

    max_prod_first = my_array[0]
    max_prod_without_first = 1
    max_now_first = my_array[0]
    max_now_without_first = 1

    for i in range(1,len(my_array)):
        max_now_first = max_now_first * my_array[i]
        max_now_without_first = max_now_without_first * my_array[i]

        if max_now_first == 0:
            max_now_first = 1
        if max_now_without_first == 0:
            max_now_without_first = 1

        if max_now_first > max_prod_first:
            max_prod_first = max_now_first

        if max_now_without_first > max_prod_without_first:
            max_prod_without_first = max_now_without_first

    if max_prod_first > max_prod_without_first:
        return max_prod_first
    else:
        return max_prod_without_first

print max_prod_sub_array(my_array=[-6])

#
# def maxProduct(A):
#     if len(A) == 0:
#         return 0
#     min_tmp = A[0]
#     max_tmp = A[0]
#     result = A[0]
#     for i in range(1, len(A)):
#         a = A[i] * min_tmp
#         b = A[i] * max_tmp
#         c = A[i]
#         max_tmp = max(max(a, b), c)
#         min_tmp = min(min(a, b), c)
#         result = max_tmp if max_tmp > result else result
#     return result
#
# print maxProduct(A=[-6,2,3])