def binary_search(lowerLimits,upperLimits,scores):
    final = [0] * len(lowerLimits)
    for i in range(len(scores)):
        for x in range(len(lowerLimits)):
            if scores[i] >= lowerLimits[x] and scores[i] <= upperLimits[x]:
                final[x] += 1
    return final

lower_arr = [2]
higher_arr = [6]
scores = [3,5,6]
print binary_search(lower_arr,higher_arr,scores)


#
#
# lower_arr = [1,2]
# higher_arr = [4,5]
# scores = [2,2,2,4,5]
# print binary_search(lower_arr,higher_arr,scores)
#
#
# def binary_search(scores,lowerLimits,upperLimits,scores):
#
#     temp = []
#     from collections import Counter
#     counter = Counter(scores)
#
#     for i in range(0,len(lowerLimits)):
#         low = lowerLimits[i]
#         high = upperLimits[i]
#         val = 0
#         for key in counter.keys():
#             if low <= key <= high:
#                 val = val + counter[key]
#         temp.append(val)
#
#     return temp


