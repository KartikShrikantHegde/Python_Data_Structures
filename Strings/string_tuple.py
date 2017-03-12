# '''
# Python concatenates adjacent string literals in any expression.
#
# >>> masters = "Mozart " 'and' " Picasso"
# >>> masters
# 'Mozart and Picasso'
# If we add commas between these strings, we'll have a tuple not a string.
#
# >>> "Mozart\"s", 'Picasso\'s'
# ('Mozart"s', "Picasso's")
# '''