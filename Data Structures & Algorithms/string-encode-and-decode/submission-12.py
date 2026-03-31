class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s))+'#'+s
        return res

    def decode(self, s: str) -> List[str]:
        # print(s)
        i=0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            # print(i, j)
            num = int(s[i:j])
            i = j+1+num
            res.append(s[j+1:i])
            # print(res)
            # i
        print(s)
        return res
