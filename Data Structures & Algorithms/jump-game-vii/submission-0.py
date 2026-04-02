class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
            
        n = len(s)
        q = [0]  
        r = 0   
        
        for i in q:
            start = max(i + minJump, r + 1)
            end = min(i + maxJump, n - 1)
            
            for j in range(start, end + 1):
                if s[j] == '0':
                    if j == n - 1:
                        return True
                    q.append(j) 
            
            r = max(r, i + maxJump)
            
        return False