class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        curr = head
        stack = []
        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
            if not curr.next and stack:
                next_node = stack.pop()
                curr.next = next_node
                next_node.prev = curr

            curr = curr.next

        return head
