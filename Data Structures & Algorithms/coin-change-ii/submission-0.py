from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(i,summ):
            if summ == amount: return 1
            if i==len(coins) or summ > amount: return 0
            return dfs(i, summ+coins[i]) + dfs(i+1, summ)
        return dfs(0,0)
