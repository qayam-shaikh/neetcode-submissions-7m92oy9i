class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch]=TrieNode()
                curr=curr.children[ch]
            curr.word = word
        row,col=len(board),len(board[0])
        ans = []
        def dfs(r,c,node):
            if r<0 or r>=row or c<0 or c>=col: return
            ch = board[r][c]
            if ch=="#" or ch not in node.children: return
            node = node.children[ch]
            if node.word:
                ans.append(node.word)
                node.word=None
            board[r][c]="#"
            dfs(r+1,c,node)
            dfs(r-1,c,node)
            dfs(r,c+1,node)
            dfs(r,c-1,node)
            board[r][c]=ch

        for r in range(row):
            for c in range(col):
                dfs(r,c,root)
        return ans
