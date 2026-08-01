class Solution(object):
    def isIsomorphic(self, s, t):
        if len (s)!=len(t):
            return False
        st={}
        ts={}
        for c1,c2 in zip(s,t):
            if c1 in st:
                if st[c1]!=c2:
                    return False
            else:
                st[c1]=c2
            if c2 in ts:
                if ts[c2]!=c1:
                    return False
            else:
                ts[c2]=c1
        return True
