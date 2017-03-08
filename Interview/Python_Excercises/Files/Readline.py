''' Used to get file -> get first line including \n from file '''

''' Only one line can be read at a time'''

'''
Open a file -> using file handler.
use the same file handler and call readline and assign to a variable.
now this variable -> holds first line of file.

The variable can be looped over to get char by char of the line
'''

f = open(filename,'r')
lines = f.readline()
print lines                  # Prints first line of file

# OR

for line in lines:           # Looping over to get char by char of first line
    print line
