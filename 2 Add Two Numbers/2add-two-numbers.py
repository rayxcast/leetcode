# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
            
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         value1 = self.composeInt(l1);
#         value2 = self.composeInt(l2);   

#         if((value1+value2) == 0):
#             return ListNode(0)
#         else:
#             return self.buildList(value1+value2)
    
#     def composeInt(self, intList):
#         current = intList;
#         n = 0;
#         value = 0;
#         while(current.val is not None):
            
#             value += current.val * pow(10,n);
            
#             if(current.next is not None):
#                 current = current.next
#                 n+=1;
#             else:
#                 break;
        
#         return value;
    
#     def buildList(self, intValue):
#         dh = ListNode(0)
#         current = dh
        
#         while(intValue > 0):
#             newNode = ListNode(intValue % 10) # create new node with value
#             current.next = newNode # set the linked list next to new node
#             current = newNode # set current to new node
#             intValue = intValue // 10
    
#         return dh.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
#         result = ListNode();
#         dummy = result;
#         sumList = 0
#         digitPlace = 1
        
#         while l1 != None and l2 != None:
#             sumList += (l1.val + l2.val) * digitPlace
#             digitPlace *= 10
#             l1 = l1.next
#             l2 = l2.next
        
#         if l1 != None:
#             while l1 != None:
#                 sumList += (l1.val) * digitPlace
#                 digitPlace *= 10
#                 l1 = l1.next
#         elif l2 != None:
#             while l2 != None:
#                 sumList += (l2.val) * digitPlace
#                 digitPlace *= 10
#                 l2 = l2.next
        
#         while sumList != 0:
#             dummy.val = sumList % 10
#             sumList = sumList // 10
            
#             if sumList != 0:
#                 dummy.next = ListNode()
#                 dummy = dummy.next
            
#         return result

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            print(columnSum)
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next
        