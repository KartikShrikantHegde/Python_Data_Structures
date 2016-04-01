#Using sorted method in tuples for keys in dictionary

my_dictionary = {'a':10,'b':20,'c':30}

#The print is unordered collections of tuples in list
print my_dictionary.items()

#Sort by key
my_tuple = sorted(my_dictionary.items())

print my_tuple

for key,value in my_tuple:
    print key,value





