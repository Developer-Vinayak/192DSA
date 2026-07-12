class Solution(object):
    def rotate(self, nums, k):
        l=len(nums)
        k=k%l
        nums[:]=nums[l-k:]+nums[:l-k]
        return nums
