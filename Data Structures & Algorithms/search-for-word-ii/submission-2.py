class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def add(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.add(word)

        rows = len(board)
        cols = len(board[0])

        res = set()
        visit = set()
        word = []
        def dfs(r, c, node):
            if (min(r, c) < 0 or r >= rows
                or c >= cols or (r,c) in visit
                or board[r][c] not in node.children):
                return

            visit.add((r,c))
            node = node.children[board[r][c]]
            word.append(board[r][c])
            if node.endOfWord:
                res.add(''.join(word))

            dfs(r+1, c, node)
            dfs(r, c+1, node)
            dfs(r-1, c, node)
            dfs(r, c-1, node)

            visit.remove((r,c))
            word.pop()
        
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return list(res)