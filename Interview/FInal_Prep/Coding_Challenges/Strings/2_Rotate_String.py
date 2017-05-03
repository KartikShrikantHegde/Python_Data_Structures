def rotate(s1,s2):
    if len(s1) == len(s2):
        s1 = s1 + s1
        if s2 in s1:
            return True
        else:
            return False
    return False


s1 = 'Karthik'
s2 = 'thikKac'
print rotate(s1,s2)