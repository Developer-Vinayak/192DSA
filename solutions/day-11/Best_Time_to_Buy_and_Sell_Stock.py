class Solution(object):
    def maxProfit(self, prices):
        min = float('inf')
        max=0
        for p in prices:
            if p<min:
                min=p
            elif p-min>max:
                max=p-min
        return max     
