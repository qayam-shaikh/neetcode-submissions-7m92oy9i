class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        res=[]
        graph={c:set() for word in words for c in word}
        state={c:0 for c in graph}
        for i in range(len(words)-1):
            w1,w2=words[i],words[i+1]
            if len(w1)>len(w2) and w1.startswith(w2):
                return ""
            for j in range(min(len(w1),len(w2))):
                if w1[j]!=w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
        def dfs(node):
            if state[node]==1:
                return True # cycle found
            elif state[node]==2:
                return False # already visited
            state[node]=1 # mark visiting
            for nei in graph[node]:
                if dfs(nei):
                    return True
            state[node]=2
            res.append(node)
            return False
        for node in graph:
            if state[node]==0:
                if dfs(node):
                    return ""
        res.reverse()
        return "".join(res)