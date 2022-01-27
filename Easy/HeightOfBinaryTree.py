# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        arr = []
        def deep(node, h):
            if node == None:
                arr.append(h)
            else:
                deep(node.left, h+1)
                deep(node.right, h+1)
                
        deep(root, 0)   
        return max(arr)
      
       
        # Failing Code
        def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_height = 0
        def deep(node, h):
            if node == None:
                if h > max_height:
                    max_height = h
                arr.append(h)
            else:
                deep(node.left, h+1)
                deep(node.right, h+1)
                
        deep(root, 0)   
        return max_height
