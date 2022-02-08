# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        all_path = []
        def binTree(node, path):
            if node == None:
                pass
            else:
                if node.left == None and node.right == None:
                    all_path.append(path+"->"+f"{node.val}")
                else:
                    binTree(node.left, path + "->"+  f"{node.val}") 
                    binTree(node.right, path + "->"+ f"{node.val}")
        
        binTree(root, "")
        answer = list(map(lambda x: x[2:], all_path))
        return answer
