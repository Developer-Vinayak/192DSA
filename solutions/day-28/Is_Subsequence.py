class Solution(object):
    def isSubsequence(self, s, t):
        st=0
        tt=0
        while st<len(s) and tt<len(t):
            if s[st]==t[tt]:
                st+=1
            tt+=1
        return len(s)==st
