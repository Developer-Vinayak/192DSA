class Solution(object):
    def isValidSudoku(self, board):
        rows = set()
        cols = set()
        boxes = set()
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                if (r, val) in rows:
                    return False
                if (c, val) in cols:
                    return False
                box_id = (r // 3, c // 3, val)
                if box_id in boxes:
                    return False
                rows.add((r, val))
                cols.add((c, val))
                boxes.add(box_id)
        return True
