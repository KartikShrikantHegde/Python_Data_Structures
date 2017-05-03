from collections import Counter
def unique(s):
    for value in Counter(s).values():
        if value > 1:
            return False
    return True

print unique('FoO')
