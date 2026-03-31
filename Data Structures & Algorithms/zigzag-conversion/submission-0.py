class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ''
        if numRows == 1:
            return s
        for i in range(numRows):
            j = i
            inc1 = (((numRows-1) - i)*2) if i != (numRows-1) else i*2
            inc2 = i*2 if i != 0 else (((numRows-1) - i)*2)
            big = True
            while j < len(s):
                res += s[j]
                if big:
                    j += inc1
                    big = False
                else:
                    j += inc2
                    big = True
        return (res)


        