''' Used to get file -> get single line by line including \n from file '''

''' Only one line can be read at a time'''

'''
Open a file -> using file handler.
use the same file handler and call readline and assign to a variable.
now this variable -> holds each line of files one after another.

The variable can be looped over to get line by line
'''

f = open(filename,'r')
lines = f.readline()
print lines                  # Prints entire file line by line

# OR

for line in lines:           # Looping over line by line
    print line