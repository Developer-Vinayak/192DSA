class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        num_rows, num_cols = len(matrix), len(matrix[0])
        directions = (0, 1, 0, -1, 0)
        visited = [[False] * num_cols for _ in range(num_rows)]
        row = col = direction_idx = 0
        result = []
        for _ in range(num_rows * num_cols):
            result.append(matrix[row][col])
            visited[row][col] = True
            next_row = row + directions[direction_idx]
            next_col = col + directions[direction_idx + 1]
            if (next_row < 0 or next_row >= num_rows or 
                next_col < 0 or next_col >= num_cols or 
                visited[next_row][next_col]):
                direction_idx = (direction_idx + 1) % 4
            row += directions[direction_idx]
            col += directions[direction_idx + 1]
        return result
