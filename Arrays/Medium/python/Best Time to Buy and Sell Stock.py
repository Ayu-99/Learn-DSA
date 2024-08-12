class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        maxRight = 0
        for i in range(len(prices)-1, -1, -1):
            maxRight = max(maxRight, prices[i])
            maxProfit = max(maxProfit, maxRight-prices[i])
        return maxProfit    
        
