class Solution:
    def preorderTraversal(self, root: 'TreeNode') -> list[int]:
        result = []
        
        def traverse(node):
            if not node:
                return
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        return result
