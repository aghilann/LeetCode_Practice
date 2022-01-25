# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer_node = ListNode()
        cur0 = answer_node
        cur1 = list1
        cur2 = list2
        
        while cur1 != None and cur2 != None:
            
            
            if cur1.val <= cur2.val:
                cur0.next = cur1
                cur1 = cur1.next
                cur0 = cur0.next
            
            elif cur1.val > cur2.val:
                cur0.next = cur2
                cur2 = cur2.next
                cur0 = cur0.next
                
        if cur1 == None:
            cur0.next = cur2
        else:
            cur0.next = cur1
        
        return answer_node.next
