class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)

        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        visit = set()

        def bfs(root):
            q = deque()
            q.append(root)
            visit.add(root) 
            
            while q:
                node = q.popleft()
                for nei in g[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)

        ct = 0
        for node in range(n): 
            if node not in visit:
                bfs(node)
                ct += 1
                
        return ct