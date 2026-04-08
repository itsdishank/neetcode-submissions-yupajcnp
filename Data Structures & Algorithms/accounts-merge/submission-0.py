class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))]
        rank = [1] * len(accounts)

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p2] >rank[p1]:
                p1, p2 = p2, p1
            
            parent[p2] = p1
            rank[p1] += rank[p2]
            return True

        emailToAcc = {}
        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                if email in emailToAcc:
                    union(i, emailToAcc[email])
                else:
                    emailToAcc[email] = i

        names = defaultdict(list)
        for k, v in emailToAcc.items():
            ind = find(v)
            names[ind].append(k)

        res = []
        for k, v in names.items():
            l = [accounts[k][0]]
            l+= (sorted(v))
            res.append(l)
        
        return res

            
            
            
        