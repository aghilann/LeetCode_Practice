# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        sumbst = []
        
        def bst(node):
            
            if node == None:
                return 0
            
            else:
                if low <= node.val <= high:
                    #sumbst.append(node.val)
                    return node.val + bst(node.left) + bst(node.right)
     
                elif low < node.val:
                    return bst(node.left)
                    
                elif high > node.val:
                    return bst(node.right)
                
        return bst(root)
