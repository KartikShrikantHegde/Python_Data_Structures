# Remove last element from list
# O(1) time

# Removing an element at the middle
# Takes O(N) time

my_list = [10,30,50]

my_list.pop()

print my_list

# Removing an element at the middle
# Takes O(N) time

# del is faster as it searches based on index value. Hence faster.
new_list = [10,30,50]

del new_list[1]

print new_list

new_list.pop(0)

print new_list

# Remove searches the value in the list and removes value. Hence slower.

new_list.remove(50)

print new_list