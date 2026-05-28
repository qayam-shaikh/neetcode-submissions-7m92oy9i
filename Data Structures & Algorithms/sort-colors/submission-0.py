class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r=w=b=0
        for x in nums:
            if x==0: r+=1
            elif x==1: w+=1
            else: b+=1
        nums[:r]=[0]*r
        nums[r:r+w]=[1]*w
        nums[r+w:r+w+b]=[2]*b


        
        