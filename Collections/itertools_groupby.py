# '''
#
#
# In this example, things is a list of tuples where the first item in each tuple is the group the second item belongs to.
#
# The groupby() function takes two arguments: (1) the data to group and (2) the function to group it with.
#
# Here, lambda x: x[0] tells groupby() to use the first item in each tuple as the grouping key.
#
# In the above for statement, groupby returns three (key, group iterator) pairs - once for each unique key. You can use the returned iterator to iterate over each individual item in that group.
# '''
#
# from itertools import groupby
#
# things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]
#
# for key, group in groupby(things, lambda x: x[0]):
#     for thing in group:
#         print "A %s is a %s." % (thing[1], key)
#     print " "
#
#
# ''''
#     A bear is a animal.
# A duck is a animal.
#
# A cactus is a plant.
#
# A speed boat is a vehicle.
# A school bus is a vehicle.
# '''

l = [4,4,4,4,5,5,5,6,7,7,7,2,2]
from itertools import groupby
for i,_ in groupby(l):
    print [(i, l.count(i))]


    # [(4, 4), (5, 3), (6, 1), (7, 3), (2, 2)]