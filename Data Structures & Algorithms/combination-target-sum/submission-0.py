class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i>=len(nums) or total >= target:
                return
            
            # stay at nums[i]
            curr.append(nums[i])
            backtrack(i, curr, total+nums[i])

            # skip nums[i]
            curr.pop()
            backtrack(i+1, curr, total)

        backtrack(0, [], 0)
        return res
            
            

            