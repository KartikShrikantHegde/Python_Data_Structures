import string

def no_of_seg_string(my_str):

    new_str = my_str.split()
    return len(new_str)


my_str = "Hello, my name is John"
print no_of_seg_string(my_str)