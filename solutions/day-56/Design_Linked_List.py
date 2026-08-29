class Node:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0) 
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    def _get_node(self, index: int) -> Node:
        if index < self.size - index:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
        return curr
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        return self._get_node(index).val
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        pred = self._get_node(index).prev if index < self.size else self.tail.prev
        succ = self._get_node(index) if index < self.size else self.tail
        pred = succ.prev
        new_node = Node(val)
        new_node.prev = pred
        new_node.next = succ
        pred.next = new_node
        succ.prev = new_node
        self.size += 1
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        node = self._get_node(index)
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
