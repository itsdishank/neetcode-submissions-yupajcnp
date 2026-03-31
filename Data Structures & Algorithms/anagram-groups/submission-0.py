class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            ss = ''.join(sorted(s))
            d[ss].append(s)
        # print(d)
        res = []

        for key in d:
            res.append(d[key])

        return res
