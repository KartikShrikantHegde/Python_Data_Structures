# # # defaultdict(int) for summing counts,
# # # and Counter() for counting list elements.
# #
# #
# # # >>> from collections import defaultdict
# # # >>> city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'), ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'), ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]
# # # >>>
# # # >>> cities_by_state = defaultdict(list)
# # # >>> for state, city in city_list:
# # # ...     cities_by_state[state].append(city)
# # # ...
# # # for state, cities in cities_by_state.iteritems():
# # # ...     print state, ', '.join(cities)
# # # ...
# # # NY Albany, Syracuse, Buffalo, Rochester
# # # CA Sacramento, Palo Alto
# # # GA Atlanta
# # # TX Austin, Houston, Dallas
# #
# #
# #
# # # It works fine here for both cases.
# #
from collections import defaultdict
from collections import Counter
#
#
name_count = [
    ("Lucy", 1),
    ("Bob", 5),
    ("Jim", 40),
    ("Susan", 6),
    ("Lucy", 2),
    ("Bob", 30),
    ("Harold", 6)
]

aggregate_counts = defaultdict(int)
for name, count in name_count:
    aggregate_counts[name] += count

print aggregate_counts
# # a,b=aggregate_counts.items()[0]
# # print a,b
# # print aggregate_counts.values()
# # #
# # # c =  Counter()
# # # for name,count in name_count:
# # #     c[name] += count
# # #
# # # print c
# #
# #
# # # ------- One More Example  -----------------
# #
# # name_count = [
# #     1,2,3,1
# # ]
# #
# # # Using Counter -> but ll print counter keyword as we are not assigning it
# #
# # print Counter(name_count)
# #
# #
# # # Using default dict
# #
# # aggregate_counts = defaultdict(int)
# # for item in name_count:
# #     aggregate_counts[item] += 1
# #
# # print aggregate_counts
#
# from collections import defaultdict
# # somedict = {}
# # print(somedict[3]) # KeyError
#
# someddict = defaultdict(int)
# print(someddict[3])
#
#
# >>> s = 'mississippi'
# >>> d = defaultdict(int)
# >>> for k in s:
# ...     d[k] += 1
# ...
# >>> d.items()
# [('i', 4), ('p', 2), ('s', 4), ('m', 1)]
# and
#
# >>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# >>> d = defaultdict(list)
# >>> for k, v in s:
# ...     d[k].append(v)
# ...
# >>> d.items()
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
#
#
# Usually, a Python dictionary throws a KeyError
# if you try to get an item with a key that is not currently in the dictionary.
# The defaultdict in contrast will simply create any items that you try to access
# (provided of course they do not exist yet). To create such a "default" item,
# it calls the function object that you pass in the constructor
# (more precisely, it's an arbitrary "callable" object, which includes function and type objects). ' \
# 'For the first example, default items are created using int(),' \
#                    ' which will return the integer object 0. For the second example,' \
#                    ' default items are created using list(), which returns a new empty list object.
