class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == '.':
                    empties.append((r, c))
                else:
                    rows[r].add(v)
                    cols[c].add(v)
                    boxes[(r // 3) * 3 + c // 3].add(v)

        digits = set("123456789")

        def solve() -> bool:
            if not empties:
                return True

            best_i = -1
            best_opts = None
            for i, (r, c) in enumerate(empties):
                opts = digits - rows[r] - cols[c] - boxes[(r // 3) * 3 + c // 3]
                if best_opts is None or len(opts) < len(best_opts):
                    best_i, best_opts = i, opts
                    if len(opts) <= 1:
                        break

            if not best_opts:
                return False

            empties[best_i], empties[-1] = empties[-1], empties[best_i]
            r, c = empties.pop()
            b = (r // 3) * 3 + c // 3

            for d in best_opts:
                board[r][c] = d
                rows[r].add(d)
                cols[c].add(d)
                boxes[b].add(d)

                if solve():
                    return True

                rows[r].remove(d)
                cols[c].remove(d)
                boxes[b].remove(d)

            board[r][c] = '.'
            empties.append((r, c))
            return False

        solve()
