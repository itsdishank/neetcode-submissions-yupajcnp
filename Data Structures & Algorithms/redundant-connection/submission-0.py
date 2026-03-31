class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank  = [1]*(n+1)
    
    def find(self, node):
        cur = node
        while cur != self.par[cur]:
            cur = self.par[cur]
        return cur
  
    def union(self, i, j):
        p1, p2 = self.find(i), self.find(j)

        if p1 == p2:
            return False
        
        if self.rank[p1] < self.rank[p2]:
            p1, p2 = p2, p1
        
        self.par[p2] = self.par[p1]
        self.rank[p1] += self.rank[p2]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        # print(dsu.par)
        for i,j in edges:
            if not dsu.union(i, j):
                return [i,j]
        

        