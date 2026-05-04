# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []  
        node = root
        prev = None
        res = []

        while node or len(stack):
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or node.right == prev:
                    res.append(node.val)
                    stack.pop()
                    prev = node
                    node = None
                else:
                    node = node.right

        return res
        
        