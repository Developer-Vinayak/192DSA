class Solution(object):
    def moveZeroes(self, nums):
        if len(nums)==1:
            return nums
        else:
            pos= 0
            for i in range(0,len(nums)):
                if nums[i]!=0:
                    temp = nums[i]
                    nums[i]=nums[pos]
                    nums[pos] = temp
                    pos+=1
        return nums   
