class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_cost = prices[0]
        maxProfit = 0
        for price in prices:
            min_cost = min(min_cost,price)
            profit = price - min_cost
            maxProfit = max(maxProfit,profit)
        return maxProfit
            
        
