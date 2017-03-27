from random import randint

table = [[] for x in range(10)]


def hash_function(x):
    # this is the method to generate a hash function. need to be a complex hash algo.
    if x == 5:
        return 8
    else:
        return 7

def insert(input):

    # print hash_function(input)

    # Note: You need to have a static hash function here which takes the
    # returned hash value and gives a new hash value because of the poor
    # hash function used. Skipped here.

    value = hash_function(input)
    table[value] = input


insert(5)
insert(5)
insert(6)

print table

