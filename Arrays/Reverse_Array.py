# Reversing an array with split,strip,and join


my_input = int(raw_input().strip())
if(my_input > 0):
    my_array = raw_input().strip().split(" ")
    print ' '.join(my_array[::-1])

'''
If split is not used it reverses character by character not the whole number. So we need split above.

my_input = int(raw_input().strip())
if(my_input > 0):
    my_array = raw_input().strip()
    print ''.join(my_array[::-1])'''



