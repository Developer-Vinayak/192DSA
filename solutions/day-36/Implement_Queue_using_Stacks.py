class MyQueue:
    def __init__(self):
        self.s = []
    def push(self, x: int) -> None:
        self.s.append(x)
        return None
    def pop(self) -> int:
        return self.s.pop(0)
    def peek(self) -> int:
        return self.s[0]
    def empty(self) -> bool:
        if self.s:  return False
        else:  return True
