class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        for i in strs:
            s+= str(len(i)) + "#" + i
        return s       


    def decode(self, s: str) -> List[str]:
        i=0
        strs = []
        while i < len(s):
            j=i
            num = ""
            while s[j] != "#":
                num += s[j]
                j +=1
            i = j + 1 + int(num)
            strs.append(s[j+1:i])
            
        return strs
