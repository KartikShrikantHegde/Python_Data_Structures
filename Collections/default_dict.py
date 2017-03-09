# defaultdict(int) for summing counts,
# and Counter() for counting list elements.

# It works fine here for both cases.

from collections import defaultdict
from collections import Counter


# name_count = [
#     ("Lucy", 1),
#     ("Bob", 5),
#     ("Jim", 40),
#     ("Susan", 6),
#     ("Lucy", 2),
#     ("Bob", 30),
#     ("Harold", 6)
# ]
#
# aggregate_counts = defaultdict(int)
# for name, count in name_count:
#     aggregate_counts[name] += count
#
# print aggregate_counts
#
# c =  Counter()
# for name,count in name_count:
#     c[name] += count
#
# print c


# ------- One More Example  -----------------

name_count = [
    1,2,3,1
]

# Using Counter -> but ll print counter keyword as we are not assigning it

print Counter(name_count)


# Using default dict

aggregate_counts = defaultdict(int)
for item in name_count:
    aggregate_counts[item] += 1

print aggregate_counts