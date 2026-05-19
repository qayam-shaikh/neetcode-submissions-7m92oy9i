# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.index = 0
        hashmap = {val:i for i, val in enumerate(inorder)}

        def create(start, end):
            if start>end: return None
            val = preorder[self.index]
            node = TreeNode(val)

            mid = hashmap[val]
            self.index += 1
            node.left = create(start, mid-1)
            node.right = create(mid+1, end)

            return node

        return create(0, len(inorder)-1)