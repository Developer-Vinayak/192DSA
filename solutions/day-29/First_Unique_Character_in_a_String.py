class Solution(object):
    def firstUniqChar(self, s):
        freq = {}
        for i in s:
            freq[i]=freq.get(i,0)+1
        for i in range(len(s)):
            x=s[i]
            if freq[x]==1:
                return i
        return -1
