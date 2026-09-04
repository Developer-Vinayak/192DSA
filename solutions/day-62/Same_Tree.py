class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]
        while stack:
            n1, n2 = stack.pop()
            if n1 is None and n2 is None:
                continue
            if n1 is None or n2 is None or n1.val != n2.val:
                return False
            stack.append((n1.left, n2.left))
            stack.append((n1.right, n2.right))
        return True
