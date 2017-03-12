my_dictionary = {'c':30,'a':10,'b':20}

#Sort by key
my_list_tuple = sorted(my_dictionary.items())
for key,value in my_list_tuple:
    print key ,"->",value

# Sort by value

my_list = list()

for key,value in my_dictionary.items():
    my_list.append((value,key))

my_list.sort()
print my_list