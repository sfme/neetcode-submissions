import heapq 

class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = [-1*i for i in stones]

        heapq.heapify(max_heap)

        while len(max_heap) > 1:

            x = heapq.heappop(max_heap) * -1
            y = heapq.heappop(max_heap) * -1

            if x == y:
                continue

            if x < y:
                stone_res = y - x

            else:
                stone_res = x - y

            heapq.heappush(max_heap, stone_res * -1)

        return max_heap[0] * -1 if len(max_heap) else 0







        