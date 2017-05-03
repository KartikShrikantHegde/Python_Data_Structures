"""
Given two binary strings,
return their sum (also a binary string).
For example,
a = "11"
b = "1"
Return "100".
"""

def sum_bin(s1,s2):
    s1 = int(s1,2)
    s2 = int(s2,2)

    s1 = s1 + s2
    return str(bin(s1))

print sum_bin("11","1")