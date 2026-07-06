class Solution(object):
    def findDisappearedNumbers(self, nums):
        nset=set(nums)
        c=[]
        for i in range(1,len(nums)+1):
           if i not in nset:
                c.append(i)
        return c
