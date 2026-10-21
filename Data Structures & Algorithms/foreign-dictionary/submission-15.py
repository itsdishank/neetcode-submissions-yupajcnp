class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adj = defaultdict(set)

        for i in range(len(words)-1):
            w1, w2 = words[i], (words[i+1])
            minLen = min(len(w1), len(w2))
            if w1[:minLen] == w2[:minLen] and len(w1)>len(w2):
                return ''
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visited = {}
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]
            
            visited[char] = True

            for nei in adj[char]:
                if dfs(nei):
                    return True
            
            visited[char] = False
            res.append(char)
        
        s = set(''.join(words))

        for char in s:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)
            