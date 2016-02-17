
def largest(something):
    max=something[0]
    for value in something:
        if value > max:
            max = value
    return max

my_list=[100,400,200,800,150,500,900]

print 'Maximum is', largest(my_list)