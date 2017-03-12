# ******** Args *************

#Eg:
# Collecting arguments
# >> > def f(*args):
#     print(args)
#
# >> > f()
# ()
# >> > f(10)
# (10,)
# >> > f(10, 20, 30)
# (10, 20, 30)

# >>> def print_all(*args):
# ...    for x in enumerate(args):
# ...       print x
# ...
# >>> print_all([1,2,3],[4,5,6])
# (0, [1, 2, 3])
# (1, [4, 5, 6])

#*********** kwargs **********


# The ** is similar but it only works
# for keyword arguments.In other words,
# it collects them into a new dictionary.
# Actually, ** allows us to convert from keywords to dictionaries:
#
# >> > def f(**kwargs):
#     print(kwargs)
#
# >> > f()
# {}
# >> > f(a=10, b=20)
# {'a': 10, 'b': 20}
# The keyword arguments is a special name = value syntax in function calls that
# specifies passing by name.It is often used to provide configuration
# options.
#
# >> > def kwargs_function(**kwargs):
#     for k, v in kwargs.items():
#         print (k, v)
#
# >> > kwargs_function(**{'uno': 'one', 'dos': 'two', 'tres': 'three'})
# ('dos', 'two')
# ('tres', 'three')
# ('uno', 'one')
# >> >
# >> > kwargs_function(dos='two', tres='three', uno='one')
# ('dos', 'two')
# ('tres', 'three')
# ('uno', 'one')
# >> >