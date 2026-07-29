class Solution(object):
    def lengthOfLastWord(self, s):
            l=s.split()
            return len(l[-1])
        
