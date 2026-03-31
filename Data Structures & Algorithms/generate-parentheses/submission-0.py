class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(cur, open, close):
            if close > open or close > n or open > n:
                return
            if close == open == n:
                res.append(cur)
                return
            
            cur += '('
            open += 1
            dfs(cur, open, close)
            cur = cur[:-1]
            open -= 1
            cur += ')'
            close += 1
            dfs(cur, open, close)

        dfs('', 0, 0)
        return res