# # Built-in Python types include integers, strings, dictionaries, lists, tuples, sets, and files.
# # which means you dont have to import them but can use them directly unlike Counter and all.
#
# # ----------------------------------------------------------------------------
#
# # In python -> Everything is object -> So no primitive types, i.e a variable holds the reference
# # to memory location, and doesnt get stored itself on the memory. Thus no concept of stack
# # memory but only heap memory.
#
#
# # -----------------------------------------------------------------------
#
# # These are python collection data types or data structures
#
# # Ordered collections are - list, tuples, strings
# # List and Tuple - Contain objects
# # Strings contain characters
# # Because they have certain order of arrangement in memory and we can access them using indexes
#
# # Strings :
# # Strings are immutable
#
# # Even when concatenated original string remains unchanged
#
# my_str = "Karthik"
# new_str = my_str + " H"
# print new_str
# print my_str
#
# # Accessing string value using indexes
# print my_str[0]
# print my_str[7]
#
# # Immutable
#
# my_str[0] = "J"
# print my_str[0]
#
#
# # Tuples :
# # Tuples are immutable
# # Tuples can have duplicate values though
#
# my_tuple = (4,5,6,6)
#
# # Another way of creating tuples is to simply put elements using comma seperated
#
# my_new_tuple = 5,6,6,[1,2,3]
# print my_new_tuple
# # print my_new_tuple                 -> (5,6,6,[1,2,3])
# #
# # Immutable
# my_tuple[1]= "Hi"
# #
# # adding elements is possible even though they are immutable and values should not be added to existing
# # tuple without creating a new tuple
#
# my_tuple = my_tuple + (7,8)
# print my_tuple
#
# # accessing tuple values using indexes
# print my_tuple[0]
#
# # Arrays are mutable - both adding and changing possible
#
# my_new_arr = []
# new_arr = list()
# my_arr = [10,20,30]
# my_arr[0] = 50
# my_arr.append(60)
#
# print my_arr
#
#
# # Unordered Collections are - sets and dict
#
# # Sets - are mutable, i.e adding an element is possible to existing set, even though you cant modify existing element
# # in sets as it cant be accessed through indexing
#
# # Sets internally use hashing of each element so that they can be stored uniquely without duplicates
#
# # Declaring set with values
#
# # my_set = {1,2,3}
#
# # Note: my_set = {}   -> this is a dict, not a set
#
# # Adding element is possible but no duplicates are allowed.
# # my_set.add(3)
# # print my_set
#
# # my_set.add(4)
# # print my_set
#
# # Using set keyword on list
#
# # l = [1, 2, 3, 3]
# # s = set(l)
# # print s
#
# # Note : you cant use indexing on sets -> print s[0] is error
#
# # Frozensets - used to get immutable sets
# # frozen = frozenset([1, 2, 3])
# # frozen.add not possible as its immutable
#
# # Dictionary

my_dict = {}
my_dict[0] = "Hello"
my_dict[10] = "Key"
for key,value in my_dict.items():
    print key,value

new_dict = {0:10,5:20}
for key,value in new_dict.items():
    print key,value

another_dict = dict()
another_dict[0] = 15
print another_dict

