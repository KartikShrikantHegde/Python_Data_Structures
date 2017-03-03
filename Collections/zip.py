# pascal triagle
#
# class Solution(object):
#     def getRow(self, rowIndex):
#         """
#         :type rowIndex: int
#         :rtype: List[int]
#         """
#         row = [1]
#         for _ in range(rowIndex):
#             row = [x + y for x, y in zip([0]+row, row+[0])]
#         return row
#
#     --------------------------------
#
#     class Solution:
#         # @return a string
#         def longestCommonPrefix(self, strs):
#             if not strs:
#                 return ""
#
#             for i, letter_group in enumerate(zip(*strs)):
#                 if len(set(letter_group)) > 1:
#                     return strs[0][:i]
#             else:
#                 return min(strs)


# This function takes two equal-length collections,
# and merges them together in pairs. if one of the collection has more len that
# extra len val is ignored for mapping
#
# It can merge 2 tuples or lists or dicts but returns list

# here key 9 is ignored as its an extra len of 2 lists

x = {1:'x', 2:'y', 3:'z',9:"v"}
y = {4:"z", 5:"a", 6:"q"}
print zip(x, y)