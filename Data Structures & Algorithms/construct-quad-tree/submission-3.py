class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def isUniform(r, c, n):
            val = grid[r][c]
            for i in range(r, r + n):
                for j in range(c, c + n):
                    if grid[i][j] != val:
                        return False
            return True

        def solve(r, c, n):
            if isUniform(r, c, n):
                return Node(grid[r][c] == 1, True, None, None, None, None)

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