class Solution(object):
    def countAndSay(self, n):
        r="1"
        for i in range(1,n):
            cur=r[0]
            new=""
            co=1
            for c in r[1:]:
                if c == cur:
                    co+=1
                else:
                    new=new+str(co)+cur
                    cur=c
                    co=1
            r=new+str(co)+cur
        return r
