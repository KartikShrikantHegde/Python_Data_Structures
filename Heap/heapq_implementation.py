# # import heapq
# #
# # heap = []
# # heapq.heappush(heap, (1, 'one'))
# # heapq.heappush(heap, (10, 'ten'))
# # heapq.heappush(heap, (5, 'five'))
# #
# # for x in heap:
# #     print x,
# # print
# #
# # heapq.heappop(heap)
# #
# # for x in heap:
# #     print x,
# # print
# #
# # # the smallest
# # print heap[0]
# #
# #
# # def heappush(heap, num):
# #     return None
# def heappush(heap, num):
# 	return None

from heapq import heappush, heappop
heap = []
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
for item in data:
    heappush(heap, item)

ordered = []
while heap:
    ordered.append(heappop(heap))

# >>> ordered
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> data.sort()
# >>> data == ordered
# True
# Using a heap to insert items at the correct place in a priority queue:
#
# >>> heap = []
# >>> data = [(1, 'J'), (4, 'N'), (3, 'H'), (2, 'O')]
# >>> for item in data:
# ...     heappush(heap, item)
# ...
# >>> while heap:
# ...     print(heappop(heap)[1])