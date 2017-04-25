# similer to list comprehension, but evaluates one at a time and syntax is diff


# Return a list of objects


my_list = [x for x in [1, 2, 3, 4, 5] if x % 2 == 0]

print my_list


# Returns a generator object
new_list = (x for x in [1, 2, 3, 4, 5] if x % 2 == 0)

print new_list
