class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxi=mini=r=nums[0]
        for n in nums[1:]:
            candidates = (n,maxi*n,mini*n)
            maxi = max(candidates)
            mini = min(candidates)
            r = max(r,maxi)
        return r
