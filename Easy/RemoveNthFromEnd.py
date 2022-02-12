# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head.next == None:
            return None
        
        slow, fast = head, head
        llen = 0
        pos = 0
        while fast or slow:
            
            if n == llen and fast == None:
                head = slow.next
                break
            
            elif fast == None:
                if llen == n:
                      if pos == llen - n:
                            slow.next = None
                            break
                elif pos == llen - n - 1:
                    slow.next = slow.next.next
                    break
                else:
                    slow = slow.next
                    pos += 1
            else:
                llen += 1
                fast = fast.next
        
        return head
                
