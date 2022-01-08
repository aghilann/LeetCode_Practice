# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = []
        # In the optimal solution, a set is used instead of an array
        cur = head
        while cur != None:
            if cur in visited:
                return True
            visited.append(cur)
            cur = cur.next
        return False
