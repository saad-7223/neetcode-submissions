class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        l , r = 0 , 1 #positions
        while r != len(prices):
            cal = prices[r] - prices[l]
            if cal < 0:
                l += 1
            else:
                r += 1
            profit = max(profit,cal)
        return profit
