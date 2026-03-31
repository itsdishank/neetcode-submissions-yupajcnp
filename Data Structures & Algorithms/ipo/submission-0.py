class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        proj = sorted(zip(capital, profits), reverse = 'True')

        # print(proj)
        maxH= []

        for _ in range(k):
            while proj and proj[-1][0]<=w:
                c, p = proj.pop()
                heapq.heappush(maxH, -p)
            if not maxH:
                return w
            
            w+= (-heapq.heappop(maxH))
        return w