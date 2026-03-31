class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
      

        zeroR = set()
        zeroC = set()

        row1 = False


        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r != 0:
                        matrix[r][0] = 0
                    else:
                        row1 = True

        # for 
        # print(matrix)

        for r in range(1,rows):
            for c in range(1, cols):
                # print(r,c)
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        # print(matrix)
        

        if matrix[0][0] == 0:
            for r in range(1, rows):
                matrix[r][0] = 0


        if row1:
            for c in range(cols):
                matrix[0][c] = 0


        # print(matrix, row1)
                # print(r,c)
        # print(zeroR, zeroC)


