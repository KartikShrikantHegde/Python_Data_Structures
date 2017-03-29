import heapq

def findKthLargest4(nums, k):

    if k == 0: return []
    heap = nums[:k]
    heapq.heapify(heap)
    for k in nums[k:]:
        if k > heap[0]:
            heapq.heapreplace(heap, k)
    return heap

nums = [1,1,1,1,1,2,2,3]
k = 2

print findKthLargest4(nums,k)