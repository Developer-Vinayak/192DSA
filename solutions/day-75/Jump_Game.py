class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for i, j in enumerate(nums):
            if i > m:
                return False
            m = max(m, i + j)
            if m>= len(nums) - 1:
                return True
        return True
