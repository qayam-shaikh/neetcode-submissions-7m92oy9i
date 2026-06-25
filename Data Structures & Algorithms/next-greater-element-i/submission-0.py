class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap={}
        stk=[]
        for num in nums2[::-1]:
            hashmap[num]=-1
            while stk and num>=stk[-1]:
                stk.pop()
            if stk:
                hashmap[num]=stk[-1]
            stk.append(num)
        ans=[]
        for num in nums1:
            ans.append(hashmap[num])
        return ans
            