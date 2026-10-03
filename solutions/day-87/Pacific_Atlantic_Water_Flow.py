from collections import deque

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])

        def bfs(starts):
            seen = set(starts)
            queue = deque(starts)
            while queue:
                r, c = queue.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m and 0 <= nc < n
                            and (nr, nc) not in seen
                            and heights[nr][nc] >= heights[r][c]):
                        seen.add((nr, nc))
                        queue.append((nr, nc))
            return seen

        pacific_starts = [(0, j) for j in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic_starts = [(m - 1, j) for j in range(n)] + [(i, n - 1) for i in range(m - 1)]

        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        return [[r, c] for r, c in pacific & atlantic]
