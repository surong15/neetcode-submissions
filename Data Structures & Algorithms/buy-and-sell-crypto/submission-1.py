class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                diff = prices[i]-buy
                if diff > profit: 
                    profit = diff
            
        return profit