class Solution(object):
    def findPeakElement(self, nums):
        m=max(nums)
        return nums.index(m)
