class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i in range(len(order)):
            d[order[i]] = i
    
        for i in range(1, len(words)):
            l1 = len(words[i-1])
            l2 = len(words[i])
            j = 0
            while j < min(l1, l2) and words[i][j] == words[i-1][j]:
                j+=1
            if j == l1 or (j < l2 and d[words[i-1][j]] < d[words[i][j]]):
                continue
            else:
                return False
        return True

                