class Solution(object):
    def topKFrequent(self, nums, k):
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        buckets=[[] for _ in range(len(nums)+1)]
        for num,f in freq.items():
            buckets[f].append(num)
        res=[]
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res)==k:
                    return res
