class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1=cand2=None
        cnt1=cnt2=0
        thres=len(nums)//3
        for n in nums:
            if n==cand1:
                cnt1+=1
            elif n==cand2:
                cnt2+=1
            elif cnt1==0:
                cand1=n
                cnt1=1
            elif cnt2==0:
                cand2=n
                cnt2=1
            else:
                cnt1-=1
                cnt2-=1
        ans=[]
        for c in (cand1,cand2):
            if c is not None and nums.count(c)>thres:
                ans.append(c)
        return ans
