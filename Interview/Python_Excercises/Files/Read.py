''' Used to get entire file -> into a string'''

''' Good if you want to say do a search and replace operation on a file'''


'''
Open a file -> using file handler.
use the same file handler and call read and assign to a variable.
now this variable is a string -> holding entire file.


Read can take size as an argument, which is the file size we want to read.
if not given it reads entire file.
 '''



''' This outputs the file as it is -> No extra space or nothing. Just as it is in the file bcz it reads file directly as a string'''

f = open(filename,'r')
lines = f.read()
print lines



''' ---------------------------- '''

''' lines gets file contents as a string here. thus we can print each character of the string or the file by looping over it'''

f = open(filename,'r')
lines = f.read()
for chars in lines:
    print chars
  
  
