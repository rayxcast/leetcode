# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(node):
            if not node:
                return
            l = node.left
            r = node.right
            invert(l)
            invert(r)
            node.left = r
            node.right = l

        invert(root)

        return root