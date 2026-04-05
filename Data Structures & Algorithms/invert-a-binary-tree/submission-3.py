#ref
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # iterative

        if not root:
            return root

        from collections import deque

        q = deque([root])
        
        while q:
            node = q.popleft()
            # Swap the children
            node.left, node.right = node.right, node.left
            
            #add children from each side
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
        return root