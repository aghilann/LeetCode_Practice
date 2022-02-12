# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even_head = ListNode()
        cur, ecur = head, even_head
        
        if head == None or head.next == None:
            return head
        
        while cur.next:
            ecur.next = cur.next
            cur.next = cur.next.next
            cur = cur.next
            if not cur.next: 
                break
            ecur = ecur.next        
        cur.next = even_head.next
        
        return head
            
