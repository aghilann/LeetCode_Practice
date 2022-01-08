# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes = {}
        lsf = 0
        cur = head
        while cur != None:
            nodes[str(lsf)] = cur
            lsf += 1
            cur = cur.next
        
        mid = lsf // 2
        return nodes.get(str(mid))
        # Used a Hashmap instead of traversing again.
                
