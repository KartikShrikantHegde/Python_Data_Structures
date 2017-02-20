table = [[] for x in range(10)]


def hash_function(x):
    # this is the method to generate a hash function. need to be a complex hash algo.
    my_has_value = x * 10
    return my_has_value % 9


def insert(input, value):

    # print hash_function(input)
    table[hash_function(input)] = value

insert(41, 'apple')
insert(93, 'banana')
insert(13, 'tangerine')

print table


#
#
# # # For resolving collision - using chaining
# #
# # table = [[] for x in range(10)]
# #
# # def insert(table,input,value):
# #     table[hash_function(input)].append((input,value))
# #     print table
# #
# # insert(table,41,'apple')
# # insert(table,93,'banana')
# # insert(table,13,'tangerine')
