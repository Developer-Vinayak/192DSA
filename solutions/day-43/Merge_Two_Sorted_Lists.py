class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d=ListNode()
        t=d
        while list1 and list2:
            if list1.val<=list2.val:
                t.next=list1
                list1=list1.next
            else:
                t.next=list2
                list2=list2.next
            t=t.next
        t.next=list1 if list1 else list2
        return d.next
