class DSU:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [1]*n

    def find(self, node):
        cur = node
        while cur != self.par[cur]:
            self.par[cur] = self.par[self.par[cur]]
            cur = self.par[cur]
        return cur

    def union(self, u, v):
        p1, p2 = self.find(u), self.find(v)

        if p1 == p2:
            return False

        if self.rank[p2]>self.rank[p1]:
            p1, p2 = p2, p1
        
        self.par[p1] = self.par[p2]
        self.rank[p1] += self.rank[p2]
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res
        
        