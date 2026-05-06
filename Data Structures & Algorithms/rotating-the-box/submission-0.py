class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows = len(boxGrid)
        cols = len(boxGrid[0])

        res = [['.'] * rows for _ in range(cols)]
        print(res)
        d = defaultdict(list)

        for r in range(rows):
            ct = 0
            for c in range(cols):
                if boxGrid[r][c] == '#':
                    ct+= 1
                elif boxGrid[r][c] == '*':
                    d[rows - 1 - r].append((c, ct))
                    ct = 0
            if ct:
                d[rows - 1 - r].append((c+1, ct))
        # print(d)
        
        for c in range(rows):
            for _ in range(len(d[c])):
                r, l = d[c].pop()
                if r < cols:
                    res[r][c] = '*'
                for nr in range(r-1, r-l-1, -1):
                    res[nr][c] = '#'

                

        return res