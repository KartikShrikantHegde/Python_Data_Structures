# Python has two build-in types of strings: str holds bytes, and unicode holds Unicode characters.
# If we only deal with 7-bit ASCII characters (characters in the range of 0-127),
# we can save some memory by using strs. However, we should be careful if we use an 8-bit character set.
# In general, it is not always possible simply by examining the bytes to determine
# which 8-bit encoding is used for a particular string.
# But the safest way is to use strs for 7-bit ASCII and for raw binary 8-bit bytes, and unicode otherwise.



# 1. str -> for bypes
# 2. unicode - for unicode characters