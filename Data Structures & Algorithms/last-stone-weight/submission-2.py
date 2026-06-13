import heapq 

class Solution:

    def lastStoneWeight(self, stones: list[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            # if x != y, the remainder is x - y; push it back as negative
            if x != y:
                heapq.heappush(max_heap, -(x - y))

        # return last remaining stone, or 0 if the heap is empty
        return -max_heap[0] if max_heap else 0


        