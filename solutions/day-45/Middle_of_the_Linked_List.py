class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        arr = []
        while cur:
            arr.append(cur)
            cur = cur.next
        return arr[len(arr) // 2]
