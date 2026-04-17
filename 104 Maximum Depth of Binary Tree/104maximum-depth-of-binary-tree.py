# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # DFS
        # def traverse(node):
        #     if not node:
        #         return 0
        #     return 1 + max(traverse(node.left), traverse(node.right))
        
        # return traverse(root)

        # BFS
        # level = 0
        # dq = deque([root])
        # while dq:
        #     for i in range(len(dq)):
        #         node = dq.popleft()
        #         if node.left:
        #             dq.append(node.left)
        #         if node.right:
        #             dq.append(node.right)
        #     level += 1
        
        # return level

        # iterative DFS
        stack = [[root, 1]]
        res = 1

        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        
        return res