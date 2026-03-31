class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = set(range(1, n+1))
        mH = []
        adjL = defaultdict(list)
        for u, v, t in times:
            adjL[u].append([v, t])
        # print(adjL)
        q = []
        heapq.heappush(q, (0, k))
        # print(q)
        ans = 0
        visit = set()
        # print()
        while q and res:
            path, node = heapq.heappop(q)
            if node in visit:
                continue
            visit.add(node)
            ans = path
            # print(path, node, ans)
            # print(q, res)
            for nei, t in adjL[node]:
                if nei not in visit:
                    heapq.heappush(q, (t+path, nei))
        # print(ans)

        return ans if len(visit) == n else -1

        