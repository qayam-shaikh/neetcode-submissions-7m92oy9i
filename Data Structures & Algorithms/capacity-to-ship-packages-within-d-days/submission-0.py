class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(cap):
            curr = 0
            total = 1
            for w in weights:
                if curr+w > cap:
                    total +=1
                    curr = w
                else:
                    curr += w
            return total <= days

        l,r= max(weights),sum(weights)
        while l<r:
            m = (l+r)//2
            if canShip(m):
                r=m
            else:
                l=m+1
        return l
