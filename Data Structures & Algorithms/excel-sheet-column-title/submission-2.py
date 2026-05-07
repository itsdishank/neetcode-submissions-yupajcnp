class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        while columnNumber > 0:
            columnNumber -= 1
            rem = columnNumber%26
            res += (chr(ord('A') + rem))
            columnNumber //= 26
            # print(columnNumber)
        return res[::-1]

        