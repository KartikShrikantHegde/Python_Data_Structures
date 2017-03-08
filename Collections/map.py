# map takes a function, and applies it to each item in an iterable (such as a list).

# map(some_function, some_iterable)

# mostly used with lamda as function


a = [1, 2, 3, 4, 5]
b = [2, 2, 9, 0, 9]


print map(  # apply the lambda to each item in the zipped list
    lambda pair: max(pair),  # pick the larger of the pair
    zip(a, b)  # create a list of tuples
)

# pasccal triangle
#
#
# def generate(self, numRows):
#     res = [[1]]
#     for i in range(1, numRows):
#         res += [map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])]
#     return res[:numRows]