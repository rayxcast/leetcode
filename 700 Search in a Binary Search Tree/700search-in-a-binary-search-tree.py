# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        head = root
        while head:
            if head.val == val:
                return head

            # look at the right subtree
            if val > head.val:
                head = head.right
            else:
            # look at the left subtree
                head = head.left
        
        return None