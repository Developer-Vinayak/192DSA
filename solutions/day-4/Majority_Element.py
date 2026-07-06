class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        nu=list(set(nums))
        for i in nu:
            c=0
            for j in nums:
                if i==j:
                    c+=1
            if c>n/2:
                return i
        return ""
