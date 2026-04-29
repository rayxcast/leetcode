# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        h = head
        start = head.next
        ac = 0

        while start:
            if start.val == 0:
                head.val = ac
                ac = 0
                if start.next:
                    head = head.next
                else:
                    break
            else:
                ac += start.val
            start = start.next
        
        head.next = None
        
        return h
        