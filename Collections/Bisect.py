# The bisect module
# This module provides functions to insert items in sorted sequences.
#
# insort(sequence, item) inserts item into the sequence, keeping it sorted. The sequence can be any mutable sequence object that implements __getitem__ and insert.
#
# Example: Using the bisect module to insert items in an ordered list
# File: bisect-example-1.py

import bisect

list = [10, 20, 30]

bisect.insort(list, 25)
bisect.insort(list, 15)

print list

# $ python bisect-example-1.py
# [10, 15, 20, 25, 30]
# bisect(sequence, item) ⇒ index returns the index where the item should be inserted. The sequence is not modified.
#
# Example: Using the bisect module to find insertion points
# File: bisect-example-2.py

import bisect

list = [10, 20, 30]

print list
print bisect.bisect(list, 25)
print bisect.bisect(list, 15)
#
# $ python bisect-example-2.py
# [10, 20, 30]
# 2
# 1