# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        arr = []
        
        while cur != None:
            arr.append(cur.val)
            cur = cur.next
        arr_len = len(arr)
        mid_index = (arr_len - 1) // 2
        for i, n in enumerate(arr):
            if n != arr[arr_len - 1 -i]:
                return False
        return True
        
