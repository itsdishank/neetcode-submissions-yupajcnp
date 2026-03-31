class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
      

        zeroR = set()
        zeroC = set()


        for r in range(rows):
            # if r in zeroR:
            #     continue
            for c in range(cols):
                # if c in zeroC:
                #     continue
                if matrix[r][c] == 0:
                    zeroR.add(r)
                    zeroC.add(c)

        for r in zeroR:
            for c in range(cols):
                matrix[r][c] = 0

        for r in range(rows):
            for c in zeroC:
                matrix[r][c] = 0
                # print(r,c)
        # print(zeroR, zeroC)


