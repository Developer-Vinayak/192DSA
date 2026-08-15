class Solution(object):
    def reverseList(self, head):
        prev=None
        cur=head
        while cur:
            nex=cur.next
            cur.next=prev
            prev=cur
            cur=nex
        return prev  
