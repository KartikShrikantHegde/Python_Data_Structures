import bisect


def kthSmallest(matrix, k):
    lo, hi = matrix[0][0], matrix[-1][-1]
    while lo < hi:
        mid = (lo + hi) // 2
        if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
            print sum(bisect.bisect_right(row, mid) for row in matrix)
            lo = mid + 1
        else:
            hi = mid
    return lo

print kthSmallest(matrix = [
             [1, 5, 9],
             [10, 11, 13],
             [12, 13, 15]
         ],
k = 8,)
