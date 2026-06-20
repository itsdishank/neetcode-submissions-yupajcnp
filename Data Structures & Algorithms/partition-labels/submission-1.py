class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastInd = defaultdict(int)
        for i, c in enumerate(s):
            lastInd[c] = i

        l = 0
        res = []
        while l<len(s):
            curEnd = r = l
            while r <= curEnd:
                curEnd = max(lastInd[s[r]], curEnd)
                r+=1
            res.append(r-l)
            l = r
            # print(l, r)

        return res
            
        