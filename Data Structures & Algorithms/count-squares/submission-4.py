class CountSquares:

    def __init__(self):
        self.d = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.d[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        ct = 0
        for (x2, y2) in self.d:
            if x1 == x2 and y1 == y2:
                continue
            if ((x1 - x2) == (y1 - y2)) or ((x1 - x2) == -(y1 - y2)):
                if (x1, y2) in self.d and (x2, y1) in self.d:
                    ct += self.d[(x1, y2)] * self.d[(x2, y1)] * self.d[(x2, y2)]
        
        return ct
