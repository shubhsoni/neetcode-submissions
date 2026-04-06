class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
            
        ans = root

        def dfs(node, ans):
            if not node:
                return ans

            if node.val > p.val and node.val > q.val:
                return dfs(node.left, ans)
            elif node.val < p.val and node.val < q.val:
                return dfs(node.right, ans)
            else:
                return node

        return dfs(root, ans)