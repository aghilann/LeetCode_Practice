# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            
            
            def recurse(pnode, qnode):
                
                if not (pnode or qnode): # Both nodes Null
                    return True
                
                elif not (pnode and qnode) or (pnode.val != qnode.val):
                    return False
                
                else:
                    return all([(recurse(pnode.left, qnode.left)), 
                                recurse(pnode.right, qnode.right)])
                    
                    
            return recurse(p, q)
