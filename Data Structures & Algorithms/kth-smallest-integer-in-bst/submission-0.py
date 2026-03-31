# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        def dfs(node):
            if not node:
                return None
            ans = dfs(node.left)
            if ans is not None:
                return ans
            self.k -= 1
            if self.k == 0:
                return node.val
            return dfs(node.right)
        
        return dfs(root)