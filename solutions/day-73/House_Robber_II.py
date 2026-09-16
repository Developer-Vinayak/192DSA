class Solution:
   def rob(self, nums):
       def rob_linear(houses):
           prev_max, curr_max = 0, 0
           for money in houses:
               prev_max, curr_max = curr_max, max(curr_max, prev_max + money)
           return curr_max
       if len(nums) == 1:
           return nums[0]
       return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))
