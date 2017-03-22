# from test.an_test.sample import Sample
#
# my_sam = Sample(10)
# print my_sam.valq

my_list = [3,6,9,11]

from collections import Counter

c = Counter(my_list)
print c.most_common()