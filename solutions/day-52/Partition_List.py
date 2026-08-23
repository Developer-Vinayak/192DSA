class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        less = less_dummy
        greater = greater_dummy
        
        cur = head
        while cur:
            if cur.val < x:
                less.next = cur
                less = less.next
            else:
                greater.next = cur
                greater = greater.next
            cur = cur.next
        
        greater.next = None 
        less.next = greater_dummy.next
        
        return less_dummy.next
