# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        output = [[]]
        def traverse(n, currLevel):
            if n is None:
                return
            # print("Current level:", currLevel)
            if len(output) < currLevel+1:
                output.append([])
            output[currLevel].append(n.val)
            # print("Current output:", output)
            traverse(n.left, currLevel+1)
            traverse(n.right, currLevel+1)

        traverse(root, 0)
        # print("Final output:", output)
        return output