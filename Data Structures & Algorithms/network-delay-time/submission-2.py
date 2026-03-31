class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g  = defaultdict(list)
        for u, v, t in times:
            g[u].append((v, t))

        print(g)

        pq = []
        pq.append((0, k))
        dist = [float('inf')]*(n+1)
        dist[k] = 0
        # ans = 0
        while pq:
            t, u = heapq.heappop(pq)
            # if u != k:
            #     ans = max(ans, dist[u])
            if dist[u] < t:
                continue
            for v, nt in g[u]:
                if dist[v] > t + nt:
                    dist[v] = t+nt
                    heapq.heappush(pq, (dist[v], v))
        # print(dist)
        # print(ans)
        ans = max(dist[1:])
        return -1 if ans == float('inf') else ans