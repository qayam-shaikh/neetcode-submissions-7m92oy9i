class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        total = sum(nums)
        pref_sum = 0
        for i in range(len(nums)):
            if i==0:
                pref_sum = 0
            else:
                pref_sum += nums[i-1]
            right_sum = (total-nums[i]-pref_sum)
            if pref_sum == right_sum:
                return i
        return -1
            