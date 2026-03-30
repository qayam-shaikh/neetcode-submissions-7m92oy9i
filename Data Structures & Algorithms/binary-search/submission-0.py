class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(nums,low,high, target):
            if low <= high:
                mid=low +(high-low)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return binary(nums, mid+1,high,target)
                else:
                    return binary(nums, low, mid-1, target)

            else:
                return -1
        
        return binary(nums,0, len(nums)-1,target)
