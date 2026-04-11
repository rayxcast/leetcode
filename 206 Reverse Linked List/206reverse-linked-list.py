# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # from collections import deque
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # stack = deque([])
        # # stack = []
        # def reverse(node):
        #     if not node:
        #         return
        #     stack.append(node.val)
        #     reverse(node.next)
        #     # print(stack)
        #     # print(node.val)
        #     node.val = stack.popleft()

        # reverse(head)
        
        # return head
        prev, curr = None, head

        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        
        return prev