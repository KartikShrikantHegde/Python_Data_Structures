#Using reverse sort method in tuples

my_dictionary = {'a':10,'b':20,'c':30}

my_list = list()

for key,value in my_dictionary.items():
    my_list.append((value,key))

print my_list

#Sort by value
my_list.sort()
print my_list

# Reverse - Sort by value
my_list.sort(reverse=True)

print my_list





