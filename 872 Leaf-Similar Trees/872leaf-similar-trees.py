# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.seq(root1) == self.seq(root2)

    def seq(self, root):
        if root.left == None and root.right == None:
            return [root.val]

        l = []
        r = []
        if root.left != None:
            l = self.seq(root.left)
        if root.right != None:
            r = self.seq(root.right)

        return l+r
        