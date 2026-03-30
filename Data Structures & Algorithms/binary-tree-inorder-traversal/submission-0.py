# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def inorder(node,res):
            if node is None:
                return
            inorder(node.left,res)
            res.append(node.val)
            inorder(node.right,res)

        res=[]
        inorder(root,res)
        return res



