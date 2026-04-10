# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        v = [-1002]
        def dfs(node):
            if not node: return True

            if not dfs(node.left):
                return False
            if node.val <= v[0]:
                return False
            v[0] = node.val
            if not dfs(node.right):
                return False
            return True

        return dfs(root)
        # return 
        