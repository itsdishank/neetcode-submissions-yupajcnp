class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res  = ''
        while columnNumber:
            columnNumber-=1
            l = columnNumber % 26
            res += chr(l+ord('A'))
            columnNumber = columnNumber // 26
        return res[::-1]