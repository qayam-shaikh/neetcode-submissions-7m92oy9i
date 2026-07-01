class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        prv=[-1]*n
        nxt=[n]*n
        stk=[]
        for i in range(n):
            while stk and heights[stk[-1]]>=heights[i]:
                stk.pop()
            if stk:
                prv[i]=stk[-1]
            stk.append(i)
        stk.clear()
        for i in range(n-1,-1,-1):
            while stk and heights[stk[-1]]>=heights[i]:
                stk.pop()
            if stk:
                nxt[i]=stk[-1]
            stk.append(i)
        area=float('-inf')
        for i in range(n):
            l,r=prv[i],nxt[i]
            width=r-l-1
            area=max(area,heights[i]*width)
        return area