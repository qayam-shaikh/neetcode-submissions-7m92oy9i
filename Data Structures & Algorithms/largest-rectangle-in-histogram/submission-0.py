class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        prev_smaller=[]
        next_smaller=[]
        stk=[]
        for i in range(len(heights)-1,-1,-1):
            while stk and heights[stk[-1]]>=heights[i]:
                stk.pop()
            next_smaller.append(stk[-1] if stk else len(heights))
            stk.append(i)
        next_smaller.reverse()
        stk.clear()
        for i in range(len(heights)):
            while stk and heights[stk[-1]]>=heights[i]:
                stk.pop()
            prev_smaller.append(stk[-1] if stk else -1)
            stk.append(i)
        ans=float('-inf')
        for i, height in enumerate(heights):
            l,r=prev_smaller[i], next_smaller[i]
            width=r-l-1
            ans=max(ans,height*width)
        return ans
