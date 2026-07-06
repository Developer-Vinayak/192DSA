class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        t=nums[0]
        for i in range(1,len(nums)):
            if t==nums[i]:
                return t
            t=nums[i]
