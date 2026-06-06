import math

class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        p_min = 1
        p_max = max(piles)

        while p_min <= p_max:

            k_val = p_min + (p_max - p_min) // 2

            # verify k_val
            time_used = 0
            for pile_i in piles:
                time_used += math.ceil(pile_i / k_val)

            if time_used > h:
                p_min = k_val + 1
            else:
                p_max = k_val - 1

        
        return p_min