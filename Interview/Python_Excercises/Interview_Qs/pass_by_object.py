# Python is pass by object -> the values passed as parameters are not copies of the values
#                             which is what Java does -> pass by value
#
# Eg:


def my_list(m):
    m.append(1)
    print m          # The value of m is same as that of l. Both point to same box

l = [0]
print l
my_list(l)
print l