# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root or (not root.left and not root.right):
            return 0
        self.curr = 0
        
        def traverseDFS(node):
            if not node:
                return 0
            left = traverseDFS(node.left)
            right = traverseDFS(node.right)
            self.curr = max(self.curr, left+right) 
            return 1 + max(left, right)
        
        traverseDFS(root)
        
        return self.curr