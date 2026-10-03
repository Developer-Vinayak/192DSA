from collections import deque
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        m, n = len(board), len(board[0])
        queue = deque()

        for i in range(m):
            for j in (0, n - 1):
                if board[i][j] == 'O':
                    board[i][j] = '#'
                    queue.append((i, j))
        for j in range(n):
            for i in (0, m - 1):
                if board[i][j] == 'O':
                    board[i][j] = '#'
                    queue.append((i, j))

        while queue:
            r, c = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O':
                    board[nr][nc] = '#'
                    queue.append((nr, nc))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
