class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
              
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        vis = set()
        def dfs(node):
            if node in vis:
                return
            vis.add(node)
            for nei in adj[node]:
                dfs(nei)
        ans = 0
        for i in range(n):
            if i not in vis:
                ans += 1
                dfs(i)
        return ans


