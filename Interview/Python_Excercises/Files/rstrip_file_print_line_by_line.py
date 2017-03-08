''' rstrip will remove the \n at the end of each line

f = open("a.txt",'r')
for line in f:
    line = line.rstrip()
    print line
