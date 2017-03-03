# String to list using split - split converts to array based on split condition

my_string = "Hi_This is a string to list example using split"

my_list = my_string.split("_")

print my_list


# String to list using list keyword - list keyword converts string to list char by char

my_str = "Hey"
print list(my_str)

# --------------------------------------------------------------------------

# List to string using join - join can be any condition, but join condition will append after 1st char

my_list = ["John","Rick","Tom"]
print "-".join(my_list)


# using string keyword - just converts the list to string

my_list = [1,2,3]
print str(my_list)


# ----------------------------------------------------------------

# str <-> int



my_str = "123"
print int(my_str)

my_int = 500
print str(my_int)

