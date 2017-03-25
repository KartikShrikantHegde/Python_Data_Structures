# def Roate_String(my_str1, my_str2):
#     for letter in my_str1:
#         if letter in my_str2 and len(my_str1)==len(my_str2):
#             continue
#         else:
#             return False
#
#     return True
#
#
# my_str1 = "abc"
# my_str2 = "cda"
#
# print Roate_String(my_str1, my_str2)



def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''

    # Check if sizes of two strings are same
    if size1 != size2:
        return 0

    # Create a temp string with value str1.str1
    temp = string1 + string1

    # Now check if str2 is a substring of temp
    # string.count returns the number of occurences of
    # the second string in temp
    x = temp.count(string2)
    print x
    if (temp.count(string2) > 0):
        return 1
    else:
        return 0


# Driver program to test the above function
string1 = "abc"
string2 = "cad"

if areRotations(string1, string2):
    print "Strings are rotations of each other"
else:
    print "Strings are not rotations of each other"