class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        listed = []
        while head is not None:
            listed.append(head.val)
            head = head.next
        return listed == listed[::-1]
