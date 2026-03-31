class CountSquares:

    def __init__(self):
        self.points = {}        

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.points[point] = self.points.get(point, 0) + 1
        

    def count(self, point: List[int]) -> int:
        qx, qy = point
        res = 0
        for x,y in self.points.keys():
            if x!=qx and y != qy and abs(qx - x) == abs(qy - y):
                if ((qx, y) in self.points) and ((x, qy) in self.points):
                    res += self.points[(x,y)] * self.points[(qx, y)] * self.points[(x, qy)]
        return res
    