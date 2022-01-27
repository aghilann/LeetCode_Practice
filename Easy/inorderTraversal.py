# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        arr = []
        def recurse(node):
            
            if node == None:
                pass
            else:
                recurse(node.left)
                arr.append(node.val)
                recurse(node.right)
        
        recurse(root)
        return arr
      
 """
Runtime: 51 ms, faster than 18.30% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13.9 MB, less than 99.93% of Python3 online submissions for Binary Tree Inorder Traversal.
"""
