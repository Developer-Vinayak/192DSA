class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        path = []
        n = len(candidates)

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, n):
                if candidates[i] > remaining:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])
                path.pop()

        backtrack(0, target)
        return result
