class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0  
        sub = []  
        for num in nums:
            idx = bisect_left(sub, num)
            if idx == len(sub):
                sub.append(num)
            else:
                sub[idx] = num

        return len(sub)
