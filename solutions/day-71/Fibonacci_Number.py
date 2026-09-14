class Solution(object):
    def fib(self, n):
        current , next = 0,1
        for _ in range(n):
            current , next = next , current + next
        return current
