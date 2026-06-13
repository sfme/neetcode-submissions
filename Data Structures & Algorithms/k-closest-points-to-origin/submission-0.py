
import math

import heapq

class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        min_heap = [(math.sqrt(math.pow(point_i[0],2) + math.pow(point_i[1],2)), point_i) for point_i in points]

        heapq.heapify(min_heap)

        res = []

        while min_heap and k:
            res.append(heapq.heappop(min_heap)[1])
            k -= 1
        
        return res

        
        
        