class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        
        while cur:
            if cur.next and cur.val == cur.next.val:
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.next
                prev.next = cur  
            else:
                prev = prev.next
                cur = cur.next
        
        return dummy.next
