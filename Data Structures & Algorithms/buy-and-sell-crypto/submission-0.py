class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        buy = float('inf')
        sell = -float('inf')
        res = 0
        for price in prices:
            if price < buy:
                buy = min(price, buy) 
                sell = price 
            sell = max(sell, price) 
            res = max(sell-buy, res)
        return res


