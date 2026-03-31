# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        s = root.val
        res = [0]
        ans = 0
        def dfs(node, s):
            if not node.left and not node.right:
                res[0] += s
                return
            if node.left:
                ts = s
                s = s*10+node.left.val
                dfs(node.left, s)
                s = ts
            if node.right:
                ts = s
                s = s*10+node.right.val
                dfs(node.right, s)
                s = ts

        dfs(root, s)
        return res[0]
        
        