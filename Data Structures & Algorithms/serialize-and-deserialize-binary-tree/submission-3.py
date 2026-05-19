# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.string = ""
        def dfs(node):
            if not node:
                self.string += "N," 
                return None
            
            self.string += str(node.val)+","
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        print(self.string)
        return self.string

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.index = 0
        data = data.split(",")
        data.pop()
        print(data)
        def dfs():
            if self.index >= len(data):
                return None

            if data[self.index]==",":
                self.index += 1
            
            if data[self.index]=="N":
                self.index += 1
                return None

            val = int(data[self.index])
            node = TreeNode(val)

            self.index += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


        