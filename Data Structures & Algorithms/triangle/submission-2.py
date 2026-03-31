class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(len(triangle) - 2, -1, -1):
            for c in range(len(triangle[row])):
                triangle[row][c] += min(triangle[row+1][c], triangle[row+1][c+1])
            
        return triangle[0][0]  
        