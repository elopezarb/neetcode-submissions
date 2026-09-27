# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        if root is None:
            return 0
        
        left = root.left
        right = root.right
        
        
        depth_l = self.maxDepth(left)
        depth_r = self.maxDepth(right)
        
        
        return max(max(self.diameterOfBinaryTree(left), self.diameterOfBinaryTree(right)), depth_l + depth_r)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        if root is None:
            return 0
        
        depth_l = self.maxDepth(root.left) + 1
        depth_r = self.maxDepth(root.right) + 1
        
        depth = max(depth_l,depth_r)
        
        return depth