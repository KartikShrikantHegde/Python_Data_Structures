import heapq

def findKthLargest4(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    for _ in xrange(len(nums)-k):
        heapq.heappop(heap)
    return heapq.heappop(heap)


nums = [8,1,1,2,3]
k = 2

print findKthLargest4(nums,k)