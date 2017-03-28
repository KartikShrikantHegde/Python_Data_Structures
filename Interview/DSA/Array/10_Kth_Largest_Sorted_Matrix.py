# def kthSmallest(matrix, k):
#     """
#     :type matrix: List[List[int]]
#     :type k: int
#     :rtype: int
#     """
#     n = len(matrix)
#     L, R = matrix[0][0], matrix[n - 1][n - 1]
#     while L < R:
#         mid = L + ((R - L) >> 1)
#         temp = sum([binary_search(y, mid, n) for y in matrix])
#         if temp < k:
#             L = mid + 1
#         else:
#             R = mid
#     return L
#
#
# def binary_search(row, x, n):
#     L, R = 0, n
#     while L < R:
#         mid = (L + R) >> 1
#         if row[mid] <= x:
#             L = mid + 1
#         else:
#             R = mid
#     return L

from heapq import heappush, heappop, heapreplace, heapify

def kthSmallest(matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        h = [(row[0], row, 1) for row in matrix]
        heapify(h)

        # Since we want to find kth, we pop the first k elements
        for _ in xrange(k - 1):
            v, r, i = h[0]
            if i < len(r):
                heapreplace(h, (r[i], r, i + 1))
            else:
                heappop(h)

        return h[0][0]

print kthSmallest(matrix = [
             [1, 5, 9],
             [10, 11, 13],
             [12, 13, 15]
         ],
k = 8,)
