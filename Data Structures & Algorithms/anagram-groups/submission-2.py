class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            l = [0] * 26
            for ch in s:
                ind = ord(ch) - ord('a')
                l[ind]+=1

            d[tuple(l)].append(s)
        # print(d)
        res = []

        for key in d:
            res.append(d[key])

        return res
