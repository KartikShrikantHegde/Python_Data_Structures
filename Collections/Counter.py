# Counter -> Keeps tracks of the no of occurances of an item as a key:value pair


from collections import Counter

my_list = [1, 2, 3, 1, 2, 3]

for k, v in Counter(my_list).items():
    print k, v
