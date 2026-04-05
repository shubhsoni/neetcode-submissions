# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def match(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val == subRoot.val:
                return match(root.left, subRoot.left) and match(root.right, subRoot.right)
            return False

        
        #traverse root untill node == subRoot
        if not root:
            return False

        stack = []
        # seen = {}
        stack = [root]
        while stack:
            node = stack.pop()
            if (node and subRoot) and (node.val == subRoot.val):
                #dont need to traverse if root and subRoot match
                if match(node, subRoot):
                    return True
               
            # seen.add(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return False