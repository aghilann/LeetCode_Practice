# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        visited = set()
        cur = head
        prev = None
        
        while cur != None:
            if cur.val in visited:
                prev.next = cur.next
                cur = cur.next
            else:
                visited.add(cur.val)
                prev = cur
                cur = cur.next
        
        return head
