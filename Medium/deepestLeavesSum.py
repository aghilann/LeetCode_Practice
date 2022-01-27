# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        arr = []
        
        max_height = [0]
        def deep(node, h):
            if node == None:
                if h > max_height[0]:
                    max_height[0] = h
                #arr.append(h)
            else:
                deep(node.left, h+1)
                deep(node.right, h+1)
                
        deep(root, 0)   
        mx = max_height[0]
        
        def deep(node, pv, h):
            if node == None:
                if h == mx:
                    arr.append(pv/2)
            else:
                deep(node.left, node.val, h + 1)
                deep(node.right, node.val, h + 1)
                
        deep(root, 0, 0)   
        
        return int(sum(arr))
 
# I acknowledge that this is a garbage algorithm.
      
  
