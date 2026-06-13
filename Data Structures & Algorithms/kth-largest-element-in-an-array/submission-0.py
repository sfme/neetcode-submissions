
import heapq

class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:

        min_heap = []
        
        for elem in nums:

            if len(min_heap) < k:
                heapq.heappush(min_heap, elem)

            elif min_heap[0] < elem:
                heapq.heapreplace(min_heap, elem)

        return min_heap[0]