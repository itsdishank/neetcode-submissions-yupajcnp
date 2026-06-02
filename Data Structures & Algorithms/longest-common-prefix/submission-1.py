class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        w = strs[0]
        
        for i in range(len(w)):
            for j in range(1, len(strs)):
                curW = strs[j]
                
                if i == len(curW) or curW[i] != w[i]:
                    return w[:i]
                    
        return w