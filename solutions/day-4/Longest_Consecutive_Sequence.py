class Solution(object):
    def longestConsecutive(self, nums):
        num=set(nums)
        l=0
        for n in num:
            if n-1 not in num:
                cur=n
                le=1
                while cur + 1 in num:
                    cur+=1
                    le+=1
                l = max(l, le)
        return l
