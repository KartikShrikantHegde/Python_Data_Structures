''' with open is another way of opening the file just like f = open("a.txt","r")'''

''' prints the file as string -> since its a read '''

with open(fileName, 'r') as f:
  line = f.read()
  print line
