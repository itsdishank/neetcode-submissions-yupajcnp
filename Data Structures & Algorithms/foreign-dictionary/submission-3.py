class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # d= {}
        # di= {}
        # for i in range(0, len(words)-1):
        #     for x, y in zip(words[i], words[i+1]):
        #         if x != y:
        #             d[x] = y
        #             di[y] = x
        

        # fi = (next(iter(di.keys())))
        # print(d, fi)

        # while fi in di:
        #     fi = di[fi]
        # # print(fi)
        # # print()
        # # print()
        # li = fi
        # res = li

        # while li in d:
        #     li = d[li]
        #     res+= li
        # # print(res)
        

        # return res
        adj = {c:set() for word in words for c in word}
        print(adj)

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
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

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)

        return words[0]

        