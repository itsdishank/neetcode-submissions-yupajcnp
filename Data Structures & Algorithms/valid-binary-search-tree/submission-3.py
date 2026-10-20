# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def dfs(minv, maxv, node):
            if not node:
                return True
            if minv < node.val < maxv:
                return dfs(minv, node.val, node.left) and dfs(node.val, maxv, node.right) 
            return False
        return dfs(float('-inf'), float('inf'), root)      