class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val:
            return root
        return self.searchBST(root.left if val < root.val else root.right, val)
