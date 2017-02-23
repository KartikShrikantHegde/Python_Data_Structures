''' Used to get file -> line by line into an array'''
''' Good if you want to loop through the file or want to do something with each line'''

'''
Open a file -> using file handler.
use the same file handler and call readlines and assign to a variable.
now this variable is a list or array -> holding each line of files one after another.
 Note: Each val in list has a \n at the end of it. bcz \n is present at the end of each line in file
 by default.

Thus you can loop over this list.
'''

f = open(filename,'r')
lines = f.readlines()
print lines

