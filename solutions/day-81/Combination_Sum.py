class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        if not candidates or target <= 0:
            return results
        candidates.sort()
        def backtrack(start: int, current_combination: List[int], current_sum: int):
            if current_sum == target:
                results.append(list(current_combination))
                return
            if current_sum > target:
                return
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                current_combination.append(candidate)
                backtrack(i, current_combination, current_sum + candidate)
                current_combination.pop()
        backtrack(0, [], 0)
        return results
