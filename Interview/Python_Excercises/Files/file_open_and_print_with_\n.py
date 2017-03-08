''' file handlers are used for file opening '''

''' Note that below lines are printed with extra new line
bcz one line from end of file having a \n character
and other new line is from print'''

f = open(filename,'r')
for line in f:
    print line
