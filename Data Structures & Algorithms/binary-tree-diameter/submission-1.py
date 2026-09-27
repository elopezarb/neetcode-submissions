# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        self.diameter = 0
        
        self.maxDepth(root)
        
        
        return self.diameter
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        if root is None:
            return 0
        
        depth_l = self.maxDepth(root.left) 
        depth_r = self.maxDepth(root.right) 
        
        depth = max(depth_l,depth_r)
        self.diameter = max(depth_l + depth_r, self.diameter)
        
        return depth + 1