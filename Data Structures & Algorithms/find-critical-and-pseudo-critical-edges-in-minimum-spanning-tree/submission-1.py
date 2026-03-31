class UnionFind:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [x for x in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        p1, p2 = self.find(a), self.find(b)
        if p1 == p2:
            return False
        if self.rank[p2] > self.rank[p1]:
            p1, p2 = p2, p1
        self.parent[p2] = p1
        self.rank[p1] += self.rank[p2]
        return True
        


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # print([x for x in range(n)])
        for i, e in enumerate(edges):
            e.append(i)

        edges.sort(key=lambda x: x[2])
        # print(edges)

        def getMST(include = -1, exclude=-1):
            uf  = UnionFind(n)
            wt = 0
            total = n
            if include != -1:
                u, v, w, _ = edges[include]
                uf.union(u,v)
                wt += w
                total-=1

            for i in range(len(edges)):
                if i == exclude:
                    continue

                u, v, w, _ = edges[i]
                if uf.union(u, v):
                    wt += w
                    total-=1
            if total > 1:
                return float('inf')
            return wt

        min_wt = getMST()
        
        critical = []
        pseudo = []
        
        for i in range(len(edges)):
            ind = edges[i][3]
            exclude_wt = getMST(exclude=i)
            include_wt = getMST(include=i)

            if exclude_wt > min_wt:
                critical.append(ind)
            elif include_wt == min_wt:
                pseudo.append(ind)
                
        return [critical, pseudo]        