class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for i in range(len(temperatures))]
        for i, v in enumerate(temperatures):
            while stack:
                # count+=1
                if temperatures[stack[-1]] < v:
                    r = stack.pop()
                    res[r] = i - r
                    # res[r] += count + (res[i] if i < len(temperatures) else 0) 
                else:
                    break
            stack.append(i)
        return res