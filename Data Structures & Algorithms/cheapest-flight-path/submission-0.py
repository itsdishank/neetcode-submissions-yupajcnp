class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for tsrc, tto, price in flights:
            graph[tsrc].append((price, tto))
        minH = [(0, -1, src)]
        visit = {(0, 0)}

        while minH:
            price, stop, node = heapq.heappop(minH)
            if stop > k:
                continue
            if node == dst:
                return price

            for nprice, nto in graph[node]:
                nprice+=price
                if (nprice+price, nto) not in visit:
                    heapq.heappush(minH, (nprice, stop+1, nto))
                    visit.add((price, nto))

        return -1
                