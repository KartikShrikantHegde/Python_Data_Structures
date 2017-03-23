
my_string = "a3b2"
temp_string = list(my_string)
res_string = []
for i in range(0,len(temp_string),2):
    x = temp_string[i] * int(temp_string[i+1])
    res_string.append(x)

print "".join(res_string)