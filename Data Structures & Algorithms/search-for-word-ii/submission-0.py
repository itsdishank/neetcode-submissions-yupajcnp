from collections import Counter
from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLUMNS = len(board), len(board[0])

        # Count board letters once
        board_count = Counter(ch for row in board for ch in row)

        # Precompute start positions by first letter to avoid scanning whole board each time
        starts = {}
        for r in range(ROWS):
            for c in range(COLUMNS):
                ch = board[r][c]
                if ch not in starts:
                    starts[ch] = []
                starts[ch].append((r, c))

        res = []

        def dfs(r: int, c: int, i: int, word: str) -> bool:
            # reached the end of the word
            if i == len(word):
                return True

            # bounds & visited check BEFORE indexing
            if r < 0 or c < 0 or r >= ROWS or c >= COLUMNS:
                return False
            if board[r][c] != word[i]:  # includes visited marker mismatch
                return False

            # mark visited in-place
            tmp = board[r][c]
            board[r][c] = "#"  # visited marker

            # explore neighbors
            found = (
                dfs(r + 1, c, i + 1, word) or
                dfs(r - 1, c, i + 1, word) or
                dfs(r, c + 1, i + 1, word) or
                dfs(r, c - 1, i + 1, word)
            )

            # restore cell
            board[r][c] = tmp
            return found

        for word in words:
            # quick prune: impossible by counts
            wc = Counter(word)
            if any(wc[ch] > board_count[ch] for ch in wc):
                continue

            # start only from cells with the first letter
            first = word[0]
            if first not in starts:
                continue

            found_this = False
            for r, c in starts[first]:
                if dfs(r, c, 0, word):
                    res.append(word)
                    found_this = True
                    break
            # optional: if not found, continue to next word automatically

        return res
