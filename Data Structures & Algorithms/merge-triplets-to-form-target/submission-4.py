class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = False
        s = set(range(len(triplets)))
        # print(s)

        for ind in range(3):
            # print(s)
            # if len(s) < 2:
            #     # print(2)
            #     return False
            cs = s.copy()
            f = False
            for t in s:
                v = triplets[t][ind]
                if v > target[ind]:
                    cs.remove(t)
                    if len(cs)<2:
                        return False
                if v == target[ind]:
                    f = True
            if not f:
                # print(3)
                return False
            s = cs


        return True

        