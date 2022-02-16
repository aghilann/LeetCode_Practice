# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        perm = ListNode()
        swap = perm
        cur = head
        
        if not cur or not cur.next:
            return cur
        
        while cur:
            if cur.next == None:
                swap.next = cur
                break
        
            go_next = cur.next.next
            swap.next = cur.next
            swap = swap.next
            swap.next = cur
            swap = swap.next
            swap.next = None
            cur = go_next      
            
        return perm.next
