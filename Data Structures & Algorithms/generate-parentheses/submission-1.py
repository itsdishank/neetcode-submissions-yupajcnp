class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        def dfs(opn, cls):
            if opn == cls == n:
                # print(cur)
                res.append(''.join(cur.copy()))
                return 
            
            if opn < n:
                cur.append('(')
                dfs(opn + 1, cls)
                cur.pop()
            
            if cls < opn:
                cur.append(')')
                dfs(opn, cls+1)
                cur.pop()
        dfs(0, 0)
        
        return res

        