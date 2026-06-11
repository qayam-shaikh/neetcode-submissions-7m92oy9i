class UnionFind:
    def __init__(self,size):
        self.parent = list(range(size))
        self.size = [1]*size
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        pa,pb=self.find(x),self.find(y)
        if pa==pb: return
        if self.size[pa]<self.size[pb]:
            pa,pb=pb,pa
        self.parent[pb]=pa
        self.size[pa]+=self.size[pb]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        uf=UnionFind(n)
        removed=None
        for u,v in edges:
            if uf.find(u-1)!=uf.find(v-1):
                uf.union(u-1,v-1)
            else:
                removed = [u,v]
        return removed