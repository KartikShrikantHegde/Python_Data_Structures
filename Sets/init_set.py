# Declaring a set - unordered collection

s = {1, 2, 3}
print s

# Using set key-word

l = [1, 2, 3, 3]
s = set(l)
print s
s.add(4)
print s

# For strings set returns a unique character by chars as a list. But its case sensitive. Eg:

my_set = "Hello! Good Day"
print set(my_set)

# o/p -> set(['!', ' ', 'e', 'd', 'G', 'H', 'l', 'o', 'a', 'y', 'D'])
