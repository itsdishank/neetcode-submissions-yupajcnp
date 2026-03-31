class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def solve(r, c, n):
            if n == 1:
                if grid[r][c] == 0:
                    v = 0
                elif grid[r][c] == 1:
                    v = 1
                return Node(v, 1, None, None, None, None)

            half = n // 2

            topLeft = solve(r, c, half)
            topRight = solve(r, c+half, half)
            bottomLeft = solve(r + half, c, half)
            bottomRight = solve(r + half, c + half, half)

            if ((topLeft.val == topRight.val == bottomLeft.val == bottomRight.val) 
            and 
            (topLeft.isLeaf == topRight.isLeaf == bottomLeft.isLeaf == bottomRight.isLeaf == 1)):
                
                isL = 1
                tl = topRight.val
                topRight = topLeft = bottomLeft = bottomRight = None
            else:
                isL = 0
                tl = 1
                
            return Node(tl, isL, topLeft, topRight, bottomLeft, bottomRight)
            
        return solve(0,0,len(grid))