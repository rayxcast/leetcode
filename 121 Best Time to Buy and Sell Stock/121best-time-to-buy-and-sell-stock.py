class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_return = 0

        l = 0
        r = 1

        while r < len(prices):
            if prices[l] < prices[r]:
                max_return = max(max_return, prices[r] - prices[l])
            else:
                l = r
            r+=1

        return max_return