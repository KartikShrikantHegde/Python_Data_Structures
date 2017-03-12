'''lambda function is a way to create small anonymous functions, i.e. functions without a name.
These functions are throw-away functions, i.e. they are just needed where they have been created.
Lambda functions are mainly used in combination with the functions filter(), map() and reduce().'''

# assuming that you have a tuple (or a pair of values), you can create a function that picks the larger of the pair:

# The general syntax of a lambda function is quite simple:
# lambda argument_list: expression

f = lambda x, y : x + y
f(1,1)


fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)
print result



a = [1, 2, 3, 4, 5]
b = [2, 2, 9, 0, 9]


print map(  # apply the lambda to each item in the zipped list
    lambda pair: max(pair),  # pick the larger of the pair
    zip(a, b)  # create a list of tuples
)