# Reversing an array with split,strip,and join

my_input = int(raw_input())
if(my_input > 0):
    my_array = list(raw_input().strip().split(' '))
    print ' '.join(my_array[::-1])