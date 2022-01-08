# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        cur1 = l1
        num1_arr = list() 
        
        while cur1 != None:
            num1_arr.append(str(cur1.val))
            cur1 = cur1.next 
        
        cur2 = l2
        num2_arr = list() 
        
        while cur2 != None:
            num2_arr.append(str(cur2.val))
            cur2 = cur2.next
        
        num1_arr.reverse()
        num2_arr.reverse()
        
        l1_string = "".join(num1_arr)
        l2_string = "".join(num2_arr)
        
        sm = int(l1_string) + int(l2_string)
        sm_string = str(sm)
        
        new_arr = [char for char in sm_string]
        new_arr.reverse()
        
        cur3 = ListNode()
        head1 = cur3
        for node in new_arr:
            cur3.next = ListNode(val=node)
            cur3 = cur3.next
        
        head1 = head1.next
        return head1
    
    # This is the first medium I solved and I found it quite challenging.
            
