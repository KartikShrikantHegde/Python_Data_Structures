# Tuple doesnt support mutable objects
# So this is not possible


my_tuple = (4,5,6)

my_tuple[2]= "Hi"

# But its possible to add items

my_tuple = my_tuple + (1,2)
print my_tuple