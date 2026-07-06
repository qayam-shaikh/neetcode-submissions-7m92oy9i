class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0: return []
        hashmap={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        ans=[]
        n=len(digits)
        def dfs(i,res):
            if i==n:
                ans.append(''.join(res))
                return
            for ch in hashmap[digits[i]]:
                res.append(ch)
                dfs(i+1,res)
                res.pop()
        dfs(0,[])
        return ans