class Solution:
    def subarraySum(self, nums, k):
        p= 0
        c= 0
        f= {0: 1}

        for num in nums:
            p+= num

            if p- k in f:
                c+= f[p - k]

            f[p] = f.get(p, 0) + 1

        return c
        
