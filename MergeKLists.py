# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if lists == []:
            return 
        
        def toNum(ll):
            
            cur = ll
            data = []
            
            while cur:
                data.append(cur.val)
                cur = cur.next
            
            return data
        
        
        # Getting rid of [] and None
        arr_of_arr = map(toNum, lists)
        #Make it all into 
        
        data = []
        
        for arr in arr_of_arr:
            data += arr
        
        data.sort()
        sorted_ll = ListNode()
        start = sorted_ll
        
        for d in data[:-1]:
            sorted_ll.val = d
            sorted_ll.next = ListNode()
            sorted_ll = sorted_ll.next
        
        if len(data) == 0:
            return None
        
        sorted_ll.val = data[-1]
        
        return start
