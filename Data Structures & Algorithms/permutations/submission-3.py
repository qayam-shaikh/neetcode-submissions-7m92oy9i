class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def bt(perm, pick, nums):
            if len(perm)==len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i]=True
                    bt(perm,pick,nums)
                    perm.pop()
                    pick[i]=False


        pick = [False]*len(nums)
        bt([],pick,nums)
        return res