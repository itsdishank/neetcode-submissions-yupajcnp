# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        node = None
        if preorder and inorder:
            node = TreeNode(preorder[0])
            inInd = (inorder.index(preorder[0]))
            del preorder[0]
            node.left = self.buildTree(preorder, inorder[0:inInd])
            node.right = self.buildTree(preorder, inorder[inInd+1:])
        return node

