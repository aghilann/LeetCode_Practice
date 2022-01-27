# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def tailRecursion(n_wl):
                
            if n_wl == []:
                return None
            
            elif n_wl[0] == None:
                return tailRecursion(n_wl[1:])
            
            elif n_wl[0].val == val:
                return n_wl[0]
            
            else:
                call = [n_wl[0].left, n_wl[0].right] + n_wl[1:]
                return tailRecursion(call)
                
        return tailRecursion([root])
