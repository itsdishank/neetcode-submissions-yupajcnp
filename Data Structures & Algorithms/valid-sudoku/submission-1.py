class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]

        rows = 9
        cols = 9

        for r in range(rows):
            rowSet = set()
            for c in range(cols):
                val = board[r][c]
                if val == '.':
                    continue
                if val in rowSet or val in colSet[c] or val in (boxSet[3*(r//3)+(c//3)]):
                    return False

                rowSet.add(val)
                colSet[c].add(val)
                boxSet[3*(r//3)+(c//3)].add(val)
    
        return True
                    