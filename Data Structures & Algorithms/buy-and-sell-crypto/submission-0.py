
class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        min_prev = prices[0]
        max_profit = 0
        
        for ii in range(1, len(prices)):
            max_profit = max(max_profit, prices[ii]-min_prev)
            min_prev = min(prices[ii], min_prev)

        return max_profit





