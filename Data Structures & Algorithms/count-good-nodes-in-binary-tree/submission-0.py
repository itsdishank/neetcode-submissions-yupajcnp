# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        curMax = root.val
        res = 0
        def dfs(node, cMax):
            if not node:
                return
            nonlocal res
            if node.val >= cMax:
                cMax = node.val
                res+=1
            dfs(node.left, cMax)
            dfs(node.right, cMax)
        
        dfs(root, curMax)
        return res
            
        