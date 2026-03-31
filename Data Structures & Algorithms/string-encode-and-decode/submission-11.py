class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+= str(len(i)) + '#' + i
        return s

    def decode(self, s: str) -> List[str]:
        res=[]
        i = 0
        while i < len(s):
            l=''
            while s[i] != '#':
                l += s[i]
                i+=1
            l = int(l)
            res.append(s[i+1:i+1+l]) 
            i += 1+l
        return res