# If ransome note can be formed out of magazine, only using magazine characters
# without repeating the characters.

from collections import Counter

def canConstruct(ransomNote, magazine):
    c = Counter(magazine)
    c.subtract(Counter(ransomNote))
    print c.values()
    return all(v >= 0 for v in c.values())

ransomNote = "aa"
magazine = "aab"
print canConstruct(ransomNote,magazine)





#
#

# import collections
#
# c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
# c2 = collections.Counter('alphabet')
#
# print 'C1:', c1
# print 'C2:', c2
#
# print '\nCombined counts:'
# print c1 + c2
#
# print '\nSubtraction:'
# print c1 - c2

