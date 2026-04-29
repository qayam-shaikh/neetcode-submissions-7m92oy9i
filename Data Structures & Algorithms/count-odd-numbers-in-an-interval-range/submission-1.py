class Solution:
    def countOdds(self, low: int, high: int) -> int:
        l = (high-low+1)
        if l&1 == 0:
            return l//2
        elif low&1==0:
            return l//2
        else:
            return l - l//2