# Counter -> Keeps tracks of the no of occurances of an item as a key:value pair
# defaultdict(int) for summing counts,
# and Counter() for counting list elements.

from collections import Counter

my_list = [1, 2, 3, 1, 2, 3]

for k, v in Counter(my_list).items():
    print k, v


# Counter also has a method called most_common that allows you to sort items by their count.
# To get the same thing in defaultdict you'll have to use sorted.
# Example:

c = Counter('aaaaaaaaabbbbbbbcc')
print c                 # Same as below but with counter type as keyword
print c.most_common()
# [('a', 9), ('b', 7), ('c', 2)]

c.most_common(2)          #return 2 most common items and their counts
# [('a', 9), ('b', 7)]

# Counter also allows you to create a list of elements from the Counter object.
# Example:

c = Counter({'a':5, 'b':3})
list(c.elements())
# ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b']
