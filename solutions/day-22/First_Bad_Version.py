class Solution(object):
    def firstBadVersion(self, n):
        low=1
        while low<n:
            mid=low+(n-low)//2
            if isBadVersion(mid):
                n =mid
            else:
                low=mid+1
        return low
