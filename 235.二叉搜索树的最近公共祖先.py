# 树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root:
            return root 
        stack = []
        ancestor = None
        while stack:
            curr = stack.pop()
            if curr == p:
            if curr == q:
            
        return preorders

        
        