# Strings also support an advance substitution known as formatting, available as both an expression and a string method call:
#
# >>>
# >>> # Formatting expression
# >>> '%s, Spain, and %s' % ('Picasso','Painting!')
# 'Picasso, Spain, and Painting!'
# >>> # Formatting method
# >>> '{0}, Spain, and {1}'.format('Pacasso', 'Painting!')
# 'Pacasso, Spain, and Painting!'
# >>>


# String Literals
# Python strings are fairly easy to use. But there are so many ways to write them in our code:
#
# >>> # Single quotes
# >>> print('P"casso')
# P"casso
#
# >>> # Double quotes
# >>> print("P'casso")
# P'casso
#
# >>> # Tripple quotes
# >>> print('''...Picasso...''')
# ...Picasso...
#
# >>> # Escape sequences
# >>> print("P\ti\nca\Osso")
# P	i
# ca\Osso
#
# >>> #Raw strings
# >>> print(r"C:\myscript.py")
# C:\myscript.py
#
# >>> # Byte strings
# >>> print(b'Picas\x01so')
# b'Picas\x01so'
# >>> type(b'Picas\x01so')
# <class 'bytes'>
# >>> type('normal_string')
# <class 'str'>
#
# >>> # Unicode strings
# >>> S = 'A\u00c4B\U000000e8C'
# >>> S
# 'A-B-C'
# >>> len(S)
# 5
# >>>