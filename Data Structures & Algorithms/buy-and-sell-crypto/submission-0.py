class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l,r=0,1
        while r<len(prices):
            sell, buy = prices[r], prices[l]
            if sell > buy:
                res = max(res,sell-buy)
            else:
                l=r
            r+=1
        return res
            