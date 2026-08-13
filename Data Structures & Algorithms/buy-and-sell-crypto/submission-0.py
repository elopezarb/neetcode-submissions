class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        L = 0
        length = len(prices)
        profit = 0
        for R in range(length):
            
            if prices[R] <= prices[L]:
                L = R
            
            profit = max(profit, prices[R]-prices[L])
        
        return profit