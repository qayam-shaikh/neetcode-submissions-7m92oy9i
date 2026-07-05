class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def dfs(o,c,res):
            if o==0 and c==0:
                ans.append(''.join(res))
                return
            if o>0:
                res.append('(')
                dfs(o-1,c,res)
                res.pop()
            if c>o:
                res.append(')')
                dfs(o,c-1,res)
                res.pop()
        dfs(n,n,[])
        return ans