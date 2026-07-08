class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count=Counter(nums)
        degree=max(count.values())
        mini=len(nums)
        for num,freq in count.items():
            if freq==degree:
                first=nums.index(num)
                last=len(nums)-1-nums[::-1].index(num)
                curr=last-first+1
                mini=min(mini, curr)
        return mini
