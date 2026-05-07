"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r, c, l):
            if l == 1:
                return Node(grid[r][c], True, None, None, None, None)
            node = Node(grid[r][c], 
                        False, 
                        dfs(r, c, l//2), 
                        dfs(r, c+(l//2), l//2), 
                        dfs(r+(l//2), c, l//2), 
                        dfs(r+(l//2), c+(l//2), l//2))
            # topLeft = dfs(r, c, l//2)
            # topRight = dfs(r, c+(l//2), l//2)
            # bottomLeft = dfs(r+(l//2), c, l//2)
            # bottomRight = dfs(r+(l//2), c+(l//2), l//2)

            v = node.topLeft.val
            if (
                node.topLeft.isLeaf and 
                node.topRight.isLeaf and 
                node.bottomLeft.isLeaf and 
                node.bottomRight.isLeaf and 
                v == node.topRight.val and 
                v == node.bottomLeft.val and 
                v == node.bottomRight.val
                ):
                node.isLeaf = True
                node.val = v
                node.topLeft = node.topRight = node.bottomRight = node.bottomLeft = None
            
            return node
        
        return dfs(0, 0, len(grid))