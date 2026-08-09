class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        start,end=0,n-1
        while start<=end:
            mid=start+(end-start)//2
            left = (mid-1+n)%n
            right = (mid+1)%n
            if nums[start]<=nums[end]:
                return nums[start]
            if nums[mid]<=nums[left] and nums[mid]<=nums[right]:
                return nums[mid]
            elif nums[mid]>=nums[0]:
                start=mid+1
            elif nums[mid]<=nums[n-1]:
                end=mid-1
        