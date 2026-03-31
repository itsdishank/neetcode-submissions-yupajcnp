class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adjL = defaultdict(list)
        for t in tickets:
            adjL[t[0]].append(t[1])
        # print(adjL)
        # sources = sorted(adjL.keys())

        res = ["JFK"]
        def dfs(s):
            if len(res) == len(tickets)+1:
                return True
            if s not in adjL:
                return False

            temp = list(adjL[s])
            for i, v in enumerate(temp):
                adjL[s].pop(i)
                res.append(v)

                if dfs(v):
                    return True
                adjL[s].insert(i, v)
                res.pop()
            return False

        dfs("JFK")
        return res
