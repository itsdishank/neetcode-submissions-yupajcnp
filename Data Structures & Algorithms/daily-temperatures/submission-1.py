class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ms = []
        res  = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            # ms.append(i)
            while len(ms)>=1 and t>temperatures[ms[-1]]:
                ind = ms.pop()
                res[ind] = i-ind
            ms.append(i)

        return res 
        