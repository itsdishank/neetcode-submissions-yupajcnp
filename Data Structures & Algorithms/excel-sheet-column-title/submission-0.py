class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res  = ''
        while columnNumber:
            l = columnNumber % 26
            if l == 0:
                res+= "Z"
                columnNumber-=1
            else:
                res += chr(l+ord('A')-1)
            columnNumber = columnNumber // 26
        return res[::-1]