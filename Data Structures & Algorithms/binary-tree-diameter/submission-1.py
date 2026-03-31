# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            if not node: return 0

            nonlocal res

            lsum = dfs(node.left)
            rsum = dfs(node.right)

            res = max(lsum+rsum, res)
            return 1+max(lsum, rsum)

        dfs(root)
        return res
        