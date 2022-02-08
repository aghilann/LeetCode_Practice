# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        node_list1 = {}
        
        cur1 = headA
        cur2 = headB
        
        while cur1:
            node_list1[cur1] = 1 
            cur1 = cur1.next
        
        while cur2:
            if node_list1.get(cur2):
                return cur2
            cur2 = cur2.next
        
        return None
