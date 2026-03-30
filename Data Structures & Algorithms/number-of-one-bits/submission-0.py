class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n>0:
            val = n%2
            n =n//2
            if val==1:
                count +=1
        return count