# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head.next == None:
            return head.next

        l = 0
        c = head

        while c:
            l += 1
            c = c.next

        c = head
        for i in range((l//2)-1):
            c = c.next
        
        c.next = c.next.next
        
        ## REMEMBER: LinkedLists use pointers so changing the values in a new variable (c) actually change the value in the orginal variable (head)
        return head