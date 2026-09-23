class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(start: int):
            if start == len(nums):
                result.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        if not isinstance(nums, list) or any(not isinstance(x, int) for x in nums):
            raise ValueError("Input must be a list of distinct integers.")
        backtrack(0)
        return result
