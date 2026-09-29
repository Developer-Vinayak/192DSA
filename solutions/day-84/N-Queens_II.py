class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diag = set()     
        anti_diag = set()  

        def backtrack(row: int) -> int:
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if col in cols or (row - col) in diag or (row + col) in anti_diag:
                    continue
                cols.add(col)
                diag.add(row - col)
                anti_diag.add(row + col)

                count += backtrack(row + 1)

                cols.remove(col)
                diag.remove(row - col)
                anti_diag.remove(row + col)
            return count

        return backtrack(0)
