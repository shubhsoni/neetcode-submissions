class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None

        #in-order traversal
        ans = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return ans[k-1]