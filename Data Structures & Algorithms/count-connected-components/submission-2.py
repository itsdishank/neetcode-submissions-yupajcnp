class DSU:
    def __init__(self, n):
        self.rank = [1]*n
        self.par = [i for i in range(n)]
        # print(self.rank, self.par)
    
    def find(self, n):
        cur = n
        while cur != self.par[cur]:
            self.par[cur] = self.par[self.par[cur]]
            cur = self.par[cur]
        return cur
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        
        if p1 == p2:
            return False
        
        if self.rank[p2] > self.rank[p1]:
            p1, p2 = p2, p1
        self.par[p2] = p1
        self.rank[p1] += self.rank[p2]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        print(n, edges)
        dsu = DSU(n)
        res = n
        for i, j in edges:
            if dsu.union(i, j):
                res -= 1

        return res