# Strings - Type-Specific Methods
# The string find method is the basic substring search operation, and the string replace method performs global searches and replacements:

S = 'Picasso'
S
# 'Picasso'
# >>>
# >>> # Find the offset of a substring
S.find('ss')
# 4

S
# 'Picasso'
# >>> # Replace occurrences of a substring with another
S.replace('ss','tt')
# 'Picatto'
S
# 'Picasso'


# >>>
# >>> line ='aaa,bbb,ccccc,dd'
# >>> # Split on a delimiter into a list of substrings
# >>> line.split(',')
# ['aaa', 'bbb', 'ccccc', 'dd']
# >>>
# >>>
# >>> S ='Picasso'
# >>>
# >>> # Upper- and lower case convedrsion
# >>> S.upper()
# 'PICASSO'
# >>> # Content tests: isalpha, isdigit, etc.
# >>> S.isalpha()
# True
# >>>
# >>> line = 'aaa,bbb,ccccc,dd\n'
# >>> # Remove whitespace characters on the right side
# >>> line = line.rstrip()
# >>> line
# 'aaa,bbb,ccccc,dd'
# >>>


# s = "a.dsfds"

# s.count('i') -> no of occurances of i in string set
# s.endswith('txt')
# False
# endswith -> returns false -> returns true if a.txt

# find('s') -> first occurancce of a word
# index - same as find but raises error if not found

# isalpha(), isdigit(), isnum(), islower(), -> all return true or false based on their conditions

# join, split,strip, replace-> some other methods

