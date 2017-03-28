import heapq

def findKthLargest4(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    for _ in xrange(len(nums)-k):
        heapq.heappop(heap)
    return heapq.heappop(heap)


nums = [10,6,9,0,8]
k = 2

print findKthLargest4(nums,k)