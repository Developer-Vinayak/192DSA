class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        from collections import Counter
        have = Counter(c for row in board for c in row)
        need = Counter(word)
        for c in need:
            if need[c] > have[c]:
                return False
        if have[word[0]] > have[word[-1]]:
            word = word[::-1]
        def bt(r, c, k):
            if k == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[k]:
                return False
            ch = board[r][c]
            board[r][c] = '#'
            res = (bt(r+1,c,k+1) or bt(r-1,c,k+1) or
                   bt(r,c+1,k+1) or bt(r,c-1,k+1))
            board[r][c] = ch
            return res
        for r in range(m):
            for c in range(n):
                if bt(r, c, 0):
                    return True
        return False
