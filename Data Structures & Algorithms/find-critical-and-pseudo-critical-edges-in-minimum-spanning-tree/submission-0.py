class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n  # Track number of connected components
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i]) # Path compression
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.count -= 1
            return True
        return False

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # 1. Preserve original indices because we will sort the array
        for i, edge in enumerate(edges):
            edge.append(i) # [u, v, w, original_index]
            
        # 2. Sort edges by weight
        edges.sort(key=lambda x: x[2])
        
        # Helper: Calculate MST weight with options to Block or Force an edge
        def get_mst_weight(block_index=-1, force_index=-1):
            uf = UnionFind(n)
            weight = 0
            
            # OPTION A: FORCE this edge to be used first (for Pseudo check)
            if force_index != -1:
                u, v, w, _ = edges[force_index]
                if uf.union(u, v):
                    weight += w
            
            # Standard Kruskal's Loop
            for i in range(len(edges)):
                if i == block_index: continue # OPTION B: BLOCK this edge (for Critical check)
                
                u, v, w, _ = edges[i]
                if uf.union(u, v):
                    weight += w
            
            # If graph is not fully connected, return Infinity
            if uf.count > 1:
                return float('inf')
                
            return weight

        # 3. Calculate the standard Minimum Weight of the MST
        min_weight = get_mst_weight()
        
        critical = []
        pseudo = []
        
        # 4. Check every edge
        for i in range(len(edges)):
            original_idx = edges[i][3]
            
            # CHECK 1: Is it CRITICAL?
            # If we delete this edge and the MST weight increases (or becomes impossible), it's critical.
            if get_mst_weight(block_index=i) > min_weight:
                critical.append(original_idx)
                
            # CHECK 2: Is it PSEUDO-CRITICAL?
            # If it's NOT critical, but FORCING it results in the same min_weight, it's pseudo-critical.
            # (This filters out "useless" heavy edges)
            elif get_mst_weight(force_index=i) == min_weight:
                pseudo.append(original_idx)
                
        return [critical, pseudo]