from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        g = defaultdict(list)
        for s, d in tickets:
            g[s].append(d)
            
        l = len(tickets) + 1
        for node in g:
            g[node].sort()
        
        cur = ['JFK']
        
        def dfs(node):
            if len(cur) == l:
                return True
                
            # Loop through the indices of available flights
            for i in range(len(g[node])):
                # Physically remove the flight so deeper recursion doesn't waste time checking it
                nei = g[node].pop(i)
                
                cur.append(nei)
                
                if dfs(nei):
                    return True
                    
                # Backtrack: pop from route and insert the ticket back into its exact sorted position
                cur.pop()
                g[node].insert(i, nei)

            return False
        
        dfs('JFK')
        return cur