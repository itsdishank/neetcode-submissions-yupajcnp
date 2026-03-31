class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtrack(i, cur):
            if i == len(digits):
                if cur:
                    res.append(cur)
                return

            for j in digitToChar[digits[i]]:
                new = cur + j
                backtrack(i+1, new)


        backtrack(0, '')
        return res
        