class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift =0
        while left < right:
            left = left >> 1
            right = right >> 1
            shift +=1 
        # we stop while when both left and right becomes same,if they have same prefix
        return left << shift