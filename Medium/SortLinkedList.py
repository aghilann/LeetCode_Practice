# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        
        cur = head
        data_ll = []
        while cur:
            data_ll.append(cur.val)
            cur = cur.next
        
        data_ll.sort()
        
        sorted_ll = ListNode()
        start = sorted_ll
        
        for data in data_ll[:-1]:
            sorted_ll.val = data
            sorted_ll.next = ListNode()
            sorted_ll = sorted_ll.next
        
        sorted_ll.val = data_ll[-1]
        
        
        return start
