class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        from collections import deque

        q = deque()
        q.append(root)
        ans = []

        while q:
            size = len(q)
            lvl = []
            for _ in range(size):
                node = q.popleft()
                if node:
                    lvl.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(lvl)

        return ans
