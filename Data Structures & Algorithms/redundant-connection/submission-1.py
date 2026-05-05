class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [1]*(n+1)

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p2] > self.rank[p1]:
            p1, p2 = p2, p1
        self.parent[p2] = p1
        self.rank[p1] += self.rank[p2]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        res = []
        dsu = DSU(len(edges))
        for a, b in edges:
            if not dsu.union(a,b):
                return [a,b]
        return res