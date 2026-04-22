class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sortP = []
        for x, y in points:
            sortP.append([x**2 + y**2, [x,y]])

        sortP.sort()
        res = []
        for i in range(k):
            res.append(sortP[i][1])
        return res